
     /*
     * This code is for an arduino connected to multiple custom current sensing boards via i2c
     * The program sampels the output from each of the boards using the i2c "wire" library and store it in an array "raw_adc" 
     * If a current drop is detected, the sensor data is then time stamped and send to a text file on a sd card module.
     * If no current drop is detected, then no data is saved. 
     *  
     *  
     */
    #include <Wire.h>
    #include <SD.h>
    #include <SPI.h>

    File myFile;
    int pinCS = 10; // Pin 10 on Arduino Uno
    int ADC_address[6]={ 0x52, 0x55,0x5A,0x50, 0x51, 0x54};
    // 0x59: 89    0x58: 88     0x51: 81    0x52: 82      0x56:86     //0x54:84(bad)   //0x5A:90
    int len = sizeof(ADC_address)/sizeof(ADC_address[0]);  //get array length
    float raw_adc[6];
    float current[6];
    float start_time=millis();
    int save =0;
    float thresh[6] ; 
    /*each board has its own current threshold. Anytime current draw of a board is below its thresh, data is saved.
    The thresh is set to the 50th current sample read from each individual board*/
    int run=1;

    
    void setup() { 
      
      Wire.begin(); //init i2c communication
      Serial.begin(9600);
      pinMode(pinCS, OUTPUT);
      
      // SD Card Initialization
      if (SD.begin()){
        Serial.println("SD card is ready to use.");
      } else{
        Serial.println("SD card initialization failed");
        return;
      }    
    }




    
    void loop() {
      delay(300);
      
      for (int i =0; i<len; i++){
          unsigned int data[2];     
          Wire.requestFrom(ADC_address[i], 2); //request 2 bytes of data
          
          if(Wire.available() == 2){
            data[0] = Wire.read();
            data[1] = Wire.read();
  }

          // Convert the data to 8 bits and calculate current
          raw_adc[i] = (((data[0] & 0x0F) * 256) + (data[1] & 0xF0)) / 16.0 ;  
          current[i]= float((245- raw_adc[i])/7.520); //VERIFIED FOR BOARDS 2 AND 3//robotics: changed from 241 to 245//maggie 7.52 for 5V, used 46 for 3v3


          //make the 50th current sample the threshold
          run=run+1;
          if (run>50 && run<56){
            
            Serial.print("----run reached------------");
            Serial.print("");
            thresh[i]=current[i];
            }

          //enter save mode if the threshold is passed
          if(((thresh[i] -current[i]) >0.1) ||(run>500 && run<506)){
            save=1;
            }

          Serial.print("raw adc "); 
          Serial.println(raw_adc[i]);
          Serial.print(ADC_address[i]);
     
          Serial.print(" current ->" );
          Serial.println( current[i]);

        }//for each data grabbing board // data acquisition

delay(500);


//----------------------------------------------
        
if (save==1){     
  // make a string for assembling the data to log:
  String dataString = "";

  // read all sensors and append to the string:
  for (int board = 0;  board< len; board++) {
    dataString += "Current:  " + String(current[board])+" Address: "+ String(ADC_address[board]);
    
    if (board < (len-1)) {
      dataString += ",";
      
    }
    else{
      float now =(millis()-start_time)/1000;
      dataString += ", Time :"+ String(now);
      save=0;
      } 
    }




  //-------------open file and save

  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
  File dataFile = SD.open("datalog.csv", FILE_WRITE);

  // if the file is available, write to it:
  Serial.println("-------------------");
  if (dataFile) {
    dataFile.println(dataString);
    dataFile.close();
    // print to the serial port too:
    
    Serial.println(dataString);
  }
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening datalog.txt");
  }
  Serial.println("-------------------");
  delay(500);
    }
    }//if



