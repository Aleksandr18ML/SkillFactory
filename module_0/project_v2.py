{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 5 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "\n",
    "def score_game(game_core):\n",
    "    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!\n",
    "    random_array = np.random.randint(1,101, size=(1000))\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)\n",
    "\n",
    "def game_core_v4(number):\n",
    "    attempts = 0           #Счетчик попыток\n",
    "    test_number = 50       #Номер для стартовой проверки \n",
    "    lownum = 0             #Минимальное число в нашем диапозоне\n",
    "    highnum = 101          #Максимальгое число в нашем диапозоне\n",
    "    step = test_number     #Шаг отслеживание \n",
    "    \n",
    "    while True:            \n",
    "        attempts +=1       \n",
    "        if number == test_number:     \n",
    "            break\n",
    "        \n",
    "        elif step == 1 and number < test_number:\n",
    "            test_number -= step\n",
    "        elif step == 1 and number > test_number:\n",
    "            test_number += step\n",
    "        \n",
    "        if number > test_number:\n",
    "            lownum = test_number + 1\n",
    "            test_number += int(step / 2)\n",
    "            step = step / 2\n",
    "        else:\n",
    "            highnum = test_number - 1\n",
    "            test_number -= int(step / 2)\n",
    "            step = step / 2\n",
    "        test_number = (lownum+highnum)//2\n",
    "        \n",
    "    return(attempts)\n",
    "\n",
    "score_game(game_core_v4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
