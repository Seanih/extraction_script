import os
import re
# /Users/Cold/Desktop/data_extraction_script/demo_log_file.txt
source_file_path = input(
    "Enter the absolute path of the source file (i.e. /Users/User/Desktop/source_file.txt): "
)

new_file_name = input(
    "Enter the name of the output file that will be created (i.e. new_file.txt): "
)

search_pattern = r"\d+\.\d+\.\d+\.\d+"

try:
    # read data from input file
    with open(source_file_path, "r") as file:
        search_results = re.findall(search_pattern, file.read())

    try:
        # give user overwrite warning
        accept_overwrite = input(
            "If a file with the name you provided already exists it will be overwritten. Do you wish to proceed? y/n: "
        )

        if accept_overwrite == "y":
            # write data to newly created file
            with open(os.getcwd() + '/' + new_file_name, "w") as file:
                # get filename from original input
                original_file = source_file_path.split("/")[-1]
                # write extracted data to new file
                file.writelines(f"All extracted findings from {original_file}:\n")
                for address in search_results:
                    file.writelines(f"{search_results.index(address) + 1}) {address}\n")

            with open(
                os.path.expanduser("~") + f"/Desktop/{new_file_name}", "r"
            ) as file:
                if file.read() != None:
                    print(f"Successfully extracted data and created {new_file_name}.")
        else:
            print("Extraction canceled.")

    except:
        print("An error occurred that prevented extraction. Please try again.")

except:
    print(
        "Either the file doesn't exist or there was an error in your input. Please try again."
    )

