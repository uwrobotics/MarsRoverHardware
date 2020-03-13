/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2020 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
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

void HAL_TIM_MspPostInit(TIM_HandleTypeDef *htim);

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define LIM_GIMB_Pin GPIO_PIN_13
#define LIM_GIMB_GPIO_Port GPIOC
#define LED_1_Pin GPIO_PIN_0
#define LED_1_GPIO_Port GPIOC
#define LED_2_Pin GPIO_PIN_1
#define LED_2_GPIO_Port GPIOC
#define LED_3_Pin GPIO_PIN_2
#define LED_3_GPIO_Port GPIOC
#define LED_4_Pin GPIO_PIN_3
#define LED_4_GPIO_Port GPIOC
#define LED_MTRX_Pin GPIO_PIN_2
#define LED_MTRX_GPIO_Port GPIOA
#define ENC_GIMB_Pin GPIO_PIN_3
#define ENC_GIMB_GPIO_Port GPIOA
#define BUTTON_1_Pin GPIO_PIN_0
#define BUTTON_1_GPIO_Port GPIOB
#define BUTTON_2_Pin GPIO_PIN_1
#define BUTTON_2_GPIO_Port GPIOB
#define CAN_RX_2_Pin GPIO_PIN_12
#define CAN_RX_2_GPIO_Port GPIOB
#define CAN_TX_2_Pin GPIO_PIN_13
#define CAN_TX_2_GPIO_Port GPIOB
#define PWM_CR_Pin GPIO_PIN_14
#define PWM_CR_GPIO_Port GPIOB
#define PWM_MG_Pin GPIO_PIN_15
#define PWM_MG_GPIO_Port GPIOB
#define CAN_RX_1_Pin GPIO_PIN_11
#define CAN_RX_1_GPIO_Port GPIOA
#define CAN_TX_1_Pin GPIO_PIN_12
#define CAN_TX_1_GPIO_Port GPIOA
#define SWD_IO_Pin GPIO_PIN_13
#define SWD_IO_GPIO_Port GPIOA
#define SWD_CLK_Pin GPIO_PIN_14
#define SWD_CLK_GPIO_Port GPIOA
#define UART_TX_Pin GPIO_PIN_10
#define UART_TX_GPIO_Port GPIOC
#define UART_RX_Pin GPIO_PIN_11
#define UART_RX_GPIO_Port GPIOC
#define ULTRA_1_TRIG_Pin GPIO_PIN_6
#define ULTRA_1_TRIG_GPIO_Port GPIOB
#define ULTRA_1_ECHO_Pin GPIO_PIN_7
#define ULTRA_1_ECHO_GPIO_Port GPIOB
#define ULTRA_2_TRIG_Pin GPIO_PIN_8
#define ULTRA_2_TRIG_GPIO_Port GPIOB
#define ULTRA_2_ECHO_Pin GPIO_PIN_9
#define ULTRA_2_ECHO_GPIO_Port GPIOB
/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
