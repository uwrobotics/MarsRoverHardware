
     /*
     * This code is for an arduino connected to multiple custom current sensing boards via i2c
     * The program sampels the output from each of the boards using the i2c "wire" library and store it in an array "raw_adc" 
     * If a current drop is detected, the sensor data is then time stamped and send to a text file on a sd card module.
     * If no current drop is detected, then no data is saved. 
     *  
     *  
     */
    #include <Wire.h>

    int ADC_address[6]={ 0x52, 0x55,0x5A,0x50, 0x51, 0x54};
    // 0x59: 89    0x58: 88     0x51: 81    0x52: 82      0x56:86     //0x54:84(bad)   //0x5A:90
    int len = sizeof(ADC_address)/sizeof(ADC_address[0]);  //get array length
    float raw_adc[6];
    float current[6];

   

    
    void setup() { 
      
      Wire.begin(); //init i2c communication
      Serial.begin(9600);
     
      

     
    }




    
    void loop() {
      
      
      for (int i =0; i<len; i++){
          unsigned int data[2];     
          Wire.requestFrom(ADC_address[i], 2); //request 2 bytes of data
          
          if(Wire.available() == 2){
            data[0] = Wire.read();
            data[1] = Wire.read();
  }

          // Convert the data to 8 bits and calculate current
          /* need to keep last 4 bits in byte 1 shift 8 bits left. Keep first 4 bits in byte 2. 
          OR the two bytes together and shift back 4 bits so that there is 1 byte of data*/
          raw_adc[i] = (((data[0] & 0x0F) * 256) + (data[1] & 0xF0)) / 16.0 ;  
          //current[i]= float((245- raw_adc[i])/7.52); //maggie 7.52 for 30A 5V, used 46 for 5A 5V, 2.253 for 100A // should work for both 5V and 3v3
          current[i]= float((246- raw_adc[i])/2.253);

         

       

          Serial.print("raw adc "); 
          Serial.println(raw_adc[i]);
          Serial.print(ADC_address[i]);
     
          Serial.print(" current ->" );
          Serial.println( current[i]);

        }//for each data grabbing board // data acquisition

delay(500);


    }




