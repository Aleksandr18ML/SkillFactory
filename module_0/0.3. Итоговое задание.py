{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-d68b6bbca03b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     35\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     36\u001b[0m     \u001b[1;32mreturn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mattempts\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 37\u001b[1;33m \u001b[0mscore_game\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mgame_core_v3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-1-d68b6bbca03b>\u001b[0m in \u001b[0;36mscore_game\u001b[1;34m(game_core)\u001b[0m\n\u001b[0;32m      8\u001b[0m     \u001b[0mrandom_array\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrandom\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrandint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m101\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msize\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1000\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mnumber\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrandom_array\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 10\u001b[1;33m         \u001b[0mcount_ls\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mgame_core\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnumber\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     11\u001b[0m     \u001b[0mscore\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcount_ls\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mf\"Ваш алгоритм угадывает число в среднем за {score} попыток\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-1-d68b6bbca03b>\u001b[0m in \u001b[0;36mgame_core_v3\u001b[1;34m(number)\u001b[0m\n\u001b[0;32m     31\u001b[0m             \u001b[0mstep\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstep\u001b[0m \u001b[1;33m/\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     32\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0mnumber\u001b[0m \u001b[1;33m<\u001b[0m \u001b[0mtest_number\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 33\u001b[1;33m             \u001b[0mtest_number\u001b[0m \u001b[1;33m-=\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstep\u001b[0m \u001b[1;33m/\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     34\u001b[0m             \u001b[0mstep\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstep\u001b[0m \u001b[1;33m/\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     35\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
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
    "def game_core_v3(number):\n",
    "    attempts = 0         #Счетчик\n",
    "    test_number = 50     #Номер проверки\n",
    "    step = test_number              \n",
    "    while True:   #условие цикла -бесконечный-\n",
    "        attempts += 1\n",
    "        if number == test_number:\n",
    "            break\n",
    "            \n",
    "        elif step == 1 and number < test_number:\n",
    "            test_number -= step\n",
    "        elif step == 1 and number > predict:\n",
    "            test_number += step\n",
    "            \n",
    "        elif number > test_number:\n",
    "            test_number += int(step / 2)\n",
    "            step = step / 2\n",
    "        elif number < test_number:\n",
    "            test_number -= int(step / 2)\n",
    "            step = step / 2\n",
    "        \n",
    "    return(attempts)\n",
    "score_game(game_core_v3)"
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
