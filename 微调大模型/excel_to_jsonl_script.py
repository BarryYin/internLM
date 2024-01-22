
import openpyxl
import json

def process_excel_to_jsonl(input_file, output_file):
    # Load the workbook and select the specified sheet
    workbook = openpyxl.load_workbook(input_file)
    sheet = workbook["5-14000"]

    # List to store the data
    data = []

    # Iterate through the rows and extract the required columns
    for row in sheet.iter_rows(min_row=2):  # Assuming the first row is headers
        input_value = row[1].value  # Column B
        output_value = row[3].value  # Column D

        # Construct the conversation object
        conversation = {
            "conversation": [
                {
                    "system": "您是一位专业、经验丰富的医生教授。您总是根据患者的问题提供准确、全面、详细的答案。",
                    "input": input_value,
                    "output": output_value
                }
            ]
        }

        # Add to the data list
        data.append(conversation)

    # Write to the output JSONL file
    with open(output_file, 'w') as f:
        for item in data:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')

# Usage
input_file_name = '5-14000.xlsx'
output_file_name = 'output.jsonl'
process_excel_to_jsonl(input_file_name, output_file_name)
