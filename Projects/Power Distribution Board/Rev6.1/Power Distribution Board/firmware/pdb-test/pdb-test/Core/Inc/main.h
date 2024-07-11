/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2023 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define FAULT_5V1_1_Pin GPIO_PIN_13
#define FAULT_5V1_1_GPIO_Port GPIOC
#define EN_5V1_1_Pin GPIO_PIN_14
#define EN_5V1_1_GPIO_Port GPIOC
#define RAIL_5V_1_Pin GPIO_PIN_15
#define RAIL_5V_1_GPIO_Port GPIOC
#define LOAD_ODRIVE_1_Pin GPIO_PIN_0
#define LOAD_ODRIVE_1_GPIO_Port GPIOC
#define EN_ODRIVE_1_Pin GPIO_PIN_1
#define EN_ODRIVE_1_GPIO_Port GPIOC
#define LOAD_ODRIVE_2_Pin GPIO_PIN_2
#define LOAD_ODRIVE_2_GPIO_Port GPIOC
#define EN_ODRIVE_2_Pin GPIO_PIN_3
#define EN_ODRIVE_2_GPIO_Port GPIOC
#define LOAD_ODRIVE_3_Pin GPIO_PIN_5
#define LOAD_ODRIVE_3_GPIO_Port GPIOA
#define EN_ODRIVE_3_Pin GPIO_PIN_6
#define EN_ODRIVE_3_GPIO_Port GPIOA
#define LOAD_VBAT_BUCK_Pin GPIO_PIN_7
#define LOAD_VBAT_BUCK_GPIO_Port GPIOA
#define RAIL_VBAT_Pin GPIO_PIN_4
#define RAIL_VBAT_GPIO_Port GPIOC
#define EN_VBAT_BUCK_Pin GPIO_PIN_5
#define EN_VBAT_BUCK_GPIO_Port GPIOC
#define RAIL_17V_Pin GPIO_PIN_0
#define RAIL_17V_GPIO_Port GPIOB
#define LOAD_17V_Pin GPIO_PIN_1
#define LOAD_17V_GPIO_Port GPIOB
#define EN_17V_Pin GPIO_PIN_2
#define EN_17V_GPIO_Port GPIOB
#define FAULT_5V2_1_Pin GPIO_PIN_10
#define FAULT_5V2_1_GPIO_Port GPIOC
#define EN_5V2_1_Pin GPIO_PIN_11
#define EN_5V2_1_GPIO_Port GPIOC
#define FAULT_5V2_2_Pin GPIO_PIN_12
#define FAULT_5V2_2_GPIO_Port GPIOC
#define EN_5V2_2_Pin GPIO_PIN_2
#define EN_5V2_2_GPIO_Port GPIOD
#define RAIL_5V_2_Pin GPIO_PIN_7
#define RAIL_5V_2_GPIO_Port GPIOB
#define FAULT_5V1_2_Pin GPIO_PIN_8
#define FAULT_5V1_2_GPIO_Port GPIOB
#define EN_5V1_2_Pin GPIO_PIN_9
#define EN_5V1_2_GPIO_Port GPIOB

/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
