{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "55d2ebe1-6e49-4153-89a2-2df8f59b8d30",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Exercise 2 complete! List of lists read from CSV:\n",
      "[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "from pathlib import Path\n",
    "\n",
    "file_path = Path(\"numbers.csv\")\n",
    "numbers = []\n",
    "\n",
    "# Read CSV file\n",
    "with open(file_path, \"r\") as file:\n",
    "    reader = csv.reader(file)\n",
    "    for row in reader:\n",
    "        numbers.append([int(num) for num in row])  # Convert to integers\n",
    "\n",
    "print(\"✅ Exercise 2 complete! List of lists read from CSV:\")\n",
    "print(numbers)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a99ff6c5-2a8e-4a13-bcda-12a57373bb37",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
