#include <stdio.h>
#include "pico/stdlib.h"
#include "pico/sleep.h"
#include "hardware/rtc.h"

#define WAKE_PIN 10
#define LED_PIN 22

int main(){
    stdio_init_all();

    gpio_init(LED_PIN);
    gpio_set_dir(WAKE_PIN, GPIO_IN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    gpio_put(LED_PIN, 0); //LED OFF

    sleep_run_from_xosc();
    sleep_goto_dormant_until_edge_high(WAKE_PIN);

    gpio_put(LED_PIN, 1); //LED ON
    while(1){
        tight_loop_contents();
    }
    return 0;
}