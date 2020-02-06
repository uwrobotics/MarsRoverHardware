/* mbed Microcontroller Library
 * Copyright (c) 2018 ARM Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"
#include "SystemReport.h"

DigitalOut led1(PC_0);
DigitalOut led2(PC_1);
DigitalOut led3(PC_2);
DigitalOut led4(PC_3);

DigitalIn pb1(PB_0);
DigitalIn pb2(PB_1);

#define SLEEP_TIME                  500 // (msec)
#define PRINT_AFTER_N_LOOPS         20

// main() runs in its own thread in the OS
int main()
{
	led1 = 0;
    led2 = 0;
    led3 = 0;
    led4 = 0;
	while(1){
    	if(!pb1){
    		led1 = 1;
    		led2 = 1;
    	}
    	else{
    		led1 = 0;
    		led2 = 0;
    	}
    	if(!pb2){
    		led3 = 1;
    		led4 = 1;
    	}
    	else{
    		led3 = 0;
    		led4 = 0;
    	}
    }


}
