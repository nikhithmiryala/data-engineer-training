import csv

def summarize_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        # Print number of rows (excluding header)
        print("Total Rows:", len(rows) - 1)
        
        # Print columns
        print("Columns:", rows[0])
        
        # Print each row
        for row in rows[1:]:
            print(row)

if __name__ == "__main__":
    summarize_csv('data.csv')
