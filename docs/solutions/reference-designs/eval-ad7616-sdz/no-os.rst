.. _eval-ad7616-sdz no-os:

No-OS driver
===============================================================================

Both the ZedBoard/ZC706 and SDP-K1 setups share a common No-OS driver for the
:adi:`AD7616`. Each setup has its own project but they reference one common
:git-no-OS:`driver <drivers/adc/ad7616>`.

Driver functions
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Function
     - Description
   * - ``int32_t ad7616_read(ad7616_dev *dev, uint8_t reg_addr, uint16_t *reg_data)``
     - SPI read from device
   * - ``int32_t ad7616_write(ad7616_dev *dev, uint8_t reg_addr, uint16_t reg_data)``
     - SPI write to device
   * - ``int32_t ad7616_read_mask(ad7616_dev *dev, uint8_t reg_addr, uint16_t mask, uint16_t *data)``
     - SPI read from device using a mask
   * - ``int32_t ad7616_write_mask(ad7616_dev *dev, uint8_t reg_addr, uint16_t mask, uint16_t data)``
     - SPI write to device using a mask
   * - ``int32_t ad7616_spi_read(ad7616_dev *dev, uint8_t reg_addr, uint16_t *reg_data)``
     - SPI read from device (low-level)
   * - ``int32_t ad7616_spi_write(ad7616_dev *dev, uint8_t reg_addr, uint16_t reg_data)``
     - SPI write to device (low-level)
   * - ``int32_t ad7616_par_read(ad7616_dev *dev, uint8_t reg_addr, uint16_t *reg_data)``
     - Parallel read from device
   * - ``int32_t ad7616_par_write(ad7616_dev *dev, uint8_t reg_addr, uint16_t reg_data)``
     - Parallel write to device
   * - ``int32_t ad7616_reset(ad7616_dev *dev)``
     - Perform a full reset of the device
   * - ``int32_t ad7616_set_range(ad7616_dev *dev, ad7616_ch ch, ad7616_range range)``
     - Set the analog input range for the selected channel
   * - ``int32_t ad7616_set_mode(ad7616_dev *dev, ad7616_mode mode)``
     - Set the operation mode (software or hardware)
   * - ``int32_t ad7616_set_oversampling_ratio(ad7616_dev *dev, ad7616_osr osr)``
     - Set the oversampling ratio
   * - ``int32_t ad7616_read_data_serial(struct ad7616_dev *dev, struct ad7616_conversion_result *results, uint32_t samples)``
     - Read conversion data in serial mode
   * - ``int32_t ad7616_setup(ad7616_dev **device, adc_core *core, ad7616_init_param init_param)``
     - Initialize the device
   * - ``int32_t ad7616_read_channel_source(struct ad7616_dev *dev, enum ad7616_ch *ch_a, enum ad7616_ch *ch_b)``
     - Read currently selected channel input sources
   * - ``int32_t ad7616_select_channel_source(struct ad7616_dev *dev, enum ad7616_ch ch)``
     - Select the input source for a channel
   * - ``int32_t ad7616_setup_sequencer(struct ad7616_dev *dev, struct ad7616_sequencer_layer *layers, uint32_t layers_nb, uint8_t burst)``
     - Set up sequencer with given layers
   * - ``int32_t ad7616_disable_sequencer(struct ad7616_dev *dev)``
     - Disable the sequencer

Driver types
-------------------------------------------------------------------------------

.. code-block:: c

   enum ad7616_mode {
       AD7616_SW,
       AD7616_HW,
   };

   enum ad7616_interface {
       AD7616_SERIAL,
       AD7616_PARALLEL,
   };

   enum ad7616_ch {
       AD7616_VA0,
       AD7616_VA1,
       AD7616_VA2,
       AD7616_VA3,
       AD7616_VA4,
       AD7616_VA5,
       AD7616_VA6,
       AD7616_VA7,
       AD7616_VA_VCC,
       AD7616_VA_ALDO,
       AD7616_VA_RESERVED1,
       AD7616_VA_SELF_TEST,
       AD7616_VA_RESERVED2,
       AD7616_VB0,
       AD7616_VB1,
       AD7616_VB2,
       AD7616_VB3,
       AD7616_VB4,
       AD7616_VB5,
       AD7616_VB6,
       AD7616_VB7,
       AD7616_VB_VCC,
       AD7616_VB_ALDO,
       AD7616_VB_RESERVED1,
       AD7616_VB_SELF_TEST,
       AD7616_VB_RESERVED2,
   };

   enum ad7616_range {
       AD7616_2V5 = 1,
       AD7616_5V  = 2,
       AD7616_10V = 3,
   };

   enum ad7616_osr {
       AD7616_OSR_0,
       AD7616_OSR_2,
       AD7616_OSR_4,
       AD7616_OSR_8,
       AD7616_OSR_16,
       AD7616_OSR_32,
       AD7616_OSR_64,
       AD7616_OSR_128,
   };

   struct ad7616_dev {
       struct no_os_spi_desc                    *spi_desc;
       struct spi_engine_offload_init_param     *offload_init_param;
       uint32_t                                  reg_access_speed;
       uint8_t                                   crc;
       struct no_os_gpio_desc                   *gpio_hw_rngsel0;
       struct no_os_gpio_desc                   *gpio_hw_rngsel1;
       struct no_os_gpio_desc                   *gpio_reset;
       struct no_os_gpio_desc                   *gpio_os0;
       struct no_os_gpio_desc                   *gpio_os1;
       struct no_os_gpio_desc                   *gpio_os2;
       struct no_os_gpio_desc                   *gpio_convst;
       struct no_os_gpio_desc                   *gpio_busy;
       uint32_t                                  core_baseaddr;
       enum ad7616_interface                     interface;
       enum ad7616_mode                          mode;
       enum ad7616_range                         va[8];
       enum ad7616_range                         vb[8];
       enum ad7616_osr                           osr;
       void (*dcache_invalidate_range)(uint32_t address, uint32_t bytes_count);
       uint8_t                                   layers_nb;
   };

   struct ad7616_init_param {
       struct no_os_spi_init_param              *spi_param;
       struct spi_engine_offload_init_param     *offload_init_param;
       uint32_t                                  reg_access_speed;
       uint8_t                                   crc;
       struct no_os_gpio_init_param             *gpio_hw_rngsel0_param;
       struct no_os_gpio_init_param             *gpio_hw_rngsel1_param;
       struct no_os_gpio_init_param             *gpio_reset_param;
       struct no_os_gpio_init_param             *gpio_os0_param;
       struct no_os_gpio_init_param             *gpio_os1_param;
       struct no_os_gpio_init_param             *gpio_os2_param;
       struct no_os_gpio_init_param             *gpio_convst_param;
       struct no_os_gpio_init_param             *gpio_busy_param;
       uint32_t                                  core_baseaddr;
       enum ad7616_mode                          mode;
       enum ad7616_range                         va[8];
       enum ad7616_range                         vb[8];
       enum ad7616_osr                           osr;
       void (*dcache_invalidate_range)(uint32_t address, uint32_t bytes_count);
   };

   struct ad7616_conversion_result {
       uint16_t channel_a;
       uint16_t channel_b;
   };

   struct ad7616_sequencer_layer {
       enum ad7616_ch ch_a;
       enum ad7616_ch ch_b;
   };

IIO driver
===============================================================================

The IIO driver wraps the base AD7616 driver to expose the device through the
IIO framework, enabling use with libiio-based tools such as IIO Oscilloscope.

IIO driver functions
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 60 40

   * - Function
     - Description
   * - ``int ad7616_iio_init(struct ad7616_iio_dev **dev, struct ad7616_init_param *init_param)``
     - Initialize the AD7616 IIO device
   * - ``int ad7616_iio_remove(struct ad7616_iio_dev *dev)``
     - Remove/free the AD7616 IIO device

IIO driver types
-------------------------------------------------------------------------------

.. code-block:: c

   struct ad7616_iio_dev {
       struct ad7616_dev  *ad7616_dev;
       struct iio_device  *iio_dev;
   };

Support
-------------------------------------------------------------------------------

For questions, visit the :adi:`EngineerZone <community>` support forums:

- `FPGA Reference Designs <https://ez.analog.com/fpga>`_
- `Microcontroller No-OS Drivers <https://ez.analog.com/microcontroller>`_
