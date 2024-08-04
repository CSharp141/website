import csv

csv_file = 'productBarcodes.csv'

with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    
    while True:
        user_input = input("Scan barcode (or 'e' to exit): ")
        
        if user_input.lower() == 'e':
            print("Exiting and saving the inputs to the CSV file.")
            break
        
        writer.writerow([user_input])

print("All inputs have been saved to", csv_file)
