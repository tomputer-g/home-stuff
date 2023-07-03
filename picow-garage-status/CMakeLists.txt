add_executable(picow_garage_status
        main.c
        )

# pull in common dependencies and additional i2c hardware support
target_link_libraries(picow_garage_status pico_stdlib hardware_i2c)

# enable usb output, disable uart output
pico_enable_stdio_usb(picow_garage_status 1)
pico_enable_stdio_uart(picow_garage_status 0)

# create map/bin/hex file etc.
pico_add_extra_outputs(picow_garage_status)
