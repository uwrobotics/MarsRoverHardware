/* mbed Microcontroller Library
 * Copyright (c) 2018 ARM Limited
 * SPDX-License-Identifier: Apache-2.0
 */

#include "mbed.h"

DigitalOut led1(PC_14);
DigitalOut led2(PC_15);
DigitalOut led3(PC_5);
DigitalOut led4(PE_15);

DigitalIn pb1(PE_3);
DigitalIn pb2(PC_13);

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
