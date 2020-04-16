# Return-Files
Simple **Python** Script to retrieve Files based on an given **pattern**.

After the project has been downloaded the file **Lits.txt** inside of the folder **"Input"** can be changed, this file contains the pattern or the patterns that the user wants to **find/copy** should be wrote on the file, different patterns on diffent lines:

For example to find all pdf files and copy them to the **Output folder** you can write:
>*.pdf

Another example, an **PDF** with a **specific name**, or all kind of files with an given name:
>*Nunes.pdf

>BigDataCracker.*

During execution of the script the user is going to be prompt to insert the **Base Path** where the script will start to search for the patterns in the filenames, the search is not only on the **Base Path** but also on the **Subdirectories**.

For example searching in my Downloads Folder for Files:
>C:\Users\jorge\Downloads

The Script as **3 Main Funtions**:
- **create_list**(Function that retrieves a List of all the patterns present in List.txt inside of Input Folder)
- **return_file**(Return the path and filename based that contains on it's name the patterns found)
- **copy_file**(Copy the file found on previous function to the folder Output)
