{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "904a63ac-0f48-489b-bafc-1531c0f948bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Exercise 4 complete! List of dictionaries read from CSV:\n",
      "[{'name': 'Joe', 'favorite_color': 'blue'}, {'name': 'Anne', 'favorite_color': 'green'}, {'name': 'Bailey', 'favorite_color': 'red'}]\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "from pathlib import Path\n",
    "\n",
    "file_path = Path(\"favorite_colors.csv\")\n",
    "favorite_colors = []\n",
    "\n",
    "# Read CSV file\n",
    "with open(file_path, \"r\") as file:\n",
    "    reader = csv.DictReader(file)\n",
    "    for row in reader:\n",
    "        favorite_colors.append(dict(row))  # Convert OrderedDict → normal dict\n",
    "\n",
    "print(\"✅ Exercise 4 complete! List of dictionaries read from CSV:\")\n",
    "print(favorite_colors)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b1924be-d965-4637-9d0a-f5395838d440",
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
