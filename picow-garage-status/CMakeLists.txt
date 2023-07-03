cmake_minimum_required(VERSION 3.13 FATAL_ERROR)

set(PICO_SDK_PATH ../../pico-sdk)
include(pico_sdk_import.cmake)
include(pico_extras_import.cmake)

project(myproject C CXX ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set(PICO_BOARD pico_w)

pico_sdk_init()

add_executable(picow_garage_status
        main.c
        )

add_executable(picow_dormant_test
        dormant_test.c
        )

# pull in common dependencies and additional i2c hardware support
target_link_libraries(picow_garage_status pico_stdlib hardware_i2c)

target_link_libraries(picow_dormant_test pico_stdlib hardware_sleep pico_cyw43_arch_none)

# enable usb output, disable uart output
pico_enable_stdio_usb(picow_garage_status 1)
pico_enable_stdio_uart(picow_garage_status 0)

# create map/bin/hex file etc.
pico_add_extra_outputs(picow_garage_status)
pico_add_extra_outputs(picow_dormant_test)
