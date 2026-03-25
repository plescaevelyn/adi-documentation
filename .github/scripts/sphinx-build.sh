#!/bin/bash

_file() {
	local f="$1"
	f="${f#$PWD/}"
	echo "$f"
}

sphinx_build() {
	local err=0
	local step_name="sphinx"
	local warnfile=$(mktemp -t sphinx.XXX)
	local docs=${1:-docs}

	pushd $docs
	sphinx-build -b html $j_ -w  "$warnfile" . _build/html -W --keep-going || err=$?
        rm -rf _build/html/_sources
	popd

	while IFS= read -r line; do
		if [[ "$line" =~ ^(.+):([0-9]+):\ (WARNING|CRITICAL|ERROR):\ (.*)$ ]]; then
			file="${BASH_REMATCH[1]}"
			lineno="${BASH_REMATCH[2]}"
			level="${BASH_REMATCH[3]}"
			msg="${BASH_REMATCH[4]}"
			[[ "$level" == "WARNING" ]] && type="warning" || type="error"
			echo "::$type file=$(_file "$file"),line=$lineno::$step_name: $msg"
		elif [[ "$line" =~ ^(.+)::\ (WARNING|CRITICAL|ERROR):\ (.*)$ ]]; then
			file="${BASH_REMATCH[1]}"
			level="${BASH_REMATCH[2]}"
			msg="${BASH_REMATCH[3]}"
			[[ "$level" == "WARNING" ]] && type="warning" || type="error"
			echo "::$type file=$(_file "$file"),line=0::$step_name: $msg"
		elif [[ "$line" =~ ^(.+):\ (WARNING|CRITICAL|ERROR):\ (.*)$ ]]; then
			file="${BASH_REMATCH[1]}"
			level="${BASH_REMATCH[2]}"
			msg="${BASH_REMATCH[3]}"
			[[ "$level" == "WARNING" ]] && type="warning" || type="error"
			echo "::$type file=$(_file "$file"),line=0::$step_name: $msg"
		fi
	done < "$warnfile"
	rm $warnfile

	return $err
}


