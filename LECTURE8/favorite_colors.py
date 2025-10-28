{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "54d69e11-016f-4dc5-821e-8f348276fc56",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Exercise 3 complete! File 'favorite_colors.csv' created at: C:\\Users\\user\\PYTHON PROGRAMMING\\LECTURE8\\favorite_colors.csv\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "from pathlib import Path\n",
    "\n",
    "file_path = Path(\"favorite_colors.csv\")\n",
    "\n",
    "favorite_colors = [\n",
    "    {\"name\": \"Joe\", \"favorite_color\": \"blue\"},\n",
    "    {\"name\": \"Anne\", \"favorite_color\": \"green\"},\n",
    "    {\"name\": \"Bailey\", \"favorite_color\": \"red\"},\n",
    "]\n",
    "\n",
    "# Write dictionaries to CSV\n",
    "with open(file_path, \"w\", newline=\"\") as file:\n",
    "    fieldnames = [\"name\", \"favorite_color\"]\n",
    "    writer = csv.DictWriter(file, fieldnames=fieldnames)\n",
    "\n",
    "    writer.writeheader()       # Write header: name,favorite_color\n",
    "    writer.writerows(favorite_colors)\n",
    "\n",
    "print(\"✅ Exercise 3 complete! File 'favorite_colors.csv' created at:\", file_path.resolve())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3311b3da-d5bb-4f27-9912-b31a480d1c67",
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
