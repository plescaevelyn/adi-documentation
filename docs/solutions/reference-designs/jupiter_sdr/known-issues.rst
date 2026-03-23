Jupiter SDR - known issues
==========================

Jupiter SDR known issues when used with `2023_r2 Patch1 Kuiper image: <https://wiki.analog.com/resources/tools-software/linux-software/adi-kuiper_images/release_notes>`_

-  IIO buffer size limited to 131072 samples when USB 3 interface is used to stream data to a host
-  USB 3 and Gigabit Ethernet interfaces throughput is currently limited by `libiio v0.26 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcdaq2-ebz/software/linux/applications/libiio>`_ implementation. The throughputs will significantly improve once libiio v1.0 will be realeaed.
-  IIO Oscilloscope profile generator (latest libadrv9002-iio) supports v68.10.1 API while 2023_r3 Patch1 comes with v68.14.10 API; `Generate a custom device profile using TES <https://wiki.analog.com/..jupiter-sdr/profile_generation_using_tes>`_
-  Multi chip synchronization support is not included in the 2023_r2 Patch1 Kuiper release. Please visit `multi-chip synchronization page <https://wiki.analog.com/resources/eval/user-guides/jupiter_sdr/mcs>`_ to check available support.
-  ADRV9002 CMOS interface not implemented
