{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6bd3c595-4f87-4567-a0b0-213a4e46a55d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Exercise 1 complete! File 'numbers.csv' created at: C:\\Users\\user\\PYTHON PROGRAMMING\\LECTURE8\\numbers.csv\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "from pathlib import Path\n",
    "\n",
    "# Create the CSV file (current directory)\n",
    "file_path = Path(\"numbers.csv\")\n",
    "\n",
    "numbers = [\n",
    "    [1, 2, 3, 4, 5],\n",
    "    [6, 7, 8, 9, 10],\n",
    "    [11, 12, 13, 14, 15],\n",
    "]\n",
    "\n",
    "# Write list of lists to CSV\n",
    "with open(file_path, \"w\", newline=\"\") as file:\n",
    "    writer = csv.writer(file)\n",
    "    writer.writerows(numbers)\n",
    "\n",
    "print(\"✅ Exercise 1 complete! File 'numbers.csv' created at:\", file_path.resolve())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7090bdb4-b51e-4277-acc3-c82c85391277",
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
