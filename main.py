import requests, subprocess, os, string, zlib


#Request to server function
def get_babel_text(hexagon_get, wall_get, shelf_get, vol_get):
    dataforurl = {"hex":hexagon_get,"wall":wall_get,"shelf":shelf_get,"volume":vol_get,"page":"1","title":"babel book"}
    url = "https://libraryofbabel.info/download.cgi"
    text = requests.post(url, data=dataforurl)
    with open("BabelBookOut.txt", "w") as f:
        f.write(text.text)

#Check if there is non-ascii chars in the given value
def check_hex_isvalid(chars):
    for i in chars:
        if i not in string.printable.replace(f"{string.ascii_uppercase}{string.punctuation}", ""):
            return False
        else:
            continue
    return True

#Check if the selected number is valid
def check_vol_isvalid(volume):
    for i in volume:
        if i not in string.digits:
            return False
        else:
            continue
    return True

#Title
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
print("\nBabel Library Book Downloader\n")

#Select mode
mode = input("Select an option (1/2/3/4/5):\n1. Use bookmark link to get single page (Recommended)\n2. Automatic mode\n3. Manual mode\n4. Convert Manual into Automatic query\n5. Exit\n> ")
subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


if mode == "1":
    selected_mode = input("Select Mode (1/2):\n1. Get page with shortened bookmark\n2. Get shortened bookmark from bookmark link\n3. Exit\n> ")
    if selected_mode == "1":
        bookmark_ID = input("\nEnter bookmark ID: ")
        url = f"https://libraryofbabel.info/bookmark.cgi?{bookmark_ID}"
        try:
            text = requests.get(url)
            text = text.text.split("<PRE id = \"textblock\">\n")[1].split("</PRE></div>")[0]
            with open("BabelPageOut.txt", "w+") as f:
                f.write(text)
            print("Successfully downloaded page\nSearch for file BabelPageOut.txt")
        except Exception as e:
            print(f"There has been an error: {e}")
    elif selected_mode == "2":
        bookmark_link = input("\nEnter bookmark link: ")
        print(f"\nBookmark ID: {bookmark_link.replace("https://libraryofbabel.info/bookmark.cgi?", "")}")
    elif selected_mode == "3":
        print("Exiting...")
        exit()
    else:
        print("Invalid mode selected")

#Automatic Mode
elif mode == "2":
    print("\nSelected Mode: Automatic\n")
    id_of_search = input("Enter ID to generate text: ").strip()
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print(f"\nSelected ID: {f"{id_of_search[:10]}..." if len(id_of_search) > 10 else id_of_search}")
    ready_for_decompression_id = f"b'{id_of_search}'"
    decompressed_id_of_search = zlib.decompress(eval(ready_for_decompression_id)).decode()
    vol = decompressed_id_of_search[-2:].replace("0", "")
    shelf = decompressed_id_of_search[-3]
    wall = decompressed_id_of_search[-4]
    hexagon = decompressed_id_of_search[:-4]
    print("\nGetting file...\nPlease wait")
    get_babel_text(hexagon, wall, shelf, vol)
    print("\nSuccessfully downloaded file!\nSearch in your current directory for a file named \"BabelBookOut.txt\"\n")
    

#Manual Mode
elif mode == "3":
    print("\nSelected Mode: Manual\n")
    hexagon = input("Enter Hexagon name: ")
    while check_hex_isvalid(hexagon) == False or not hexagon:
        hexagon = input("\nEnter Hexagon name: ")
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    print(f"\nSelected Hexagon: {f"{hexagon[:10]}..." if len(hexagon) > 10 else hexagon}")
    
    wall = input("Enter Wall number (1-4): ")
    while not wall or not wall in string.digits or int(wall) > 4 or int(wall) < 1:
        wall = input("Enter Wall number (1-4): ")
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    print(f"\nSelected Hexagon: {f"{hexagon[:10]}..." if len(hexagon) > 10 else hexagon}")
    print(f"Selected Wall: {wall}")
    
    shelf = input("Enter Shelf number (1-5): ")
    while not shelf or not shelf in string.digits or int(shelf) > 5 or int(shelf) < 1:
        shelf = input("Enter Shelf number (1-5): ")
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    print(f"\nSelected Hexagon: {f"{hexagon[:10]}..." if len(hexagon) > 10 else hexagon}")
    print(f"Selected Wall: {wall}")
    print(f"Selected Shelf: {shelf}")
    
    vol = input("Enter Volume number (1-32): ")
    while not vol or check_vol_isvalid(vol) == False or int(vol) > 32 or int(vol) < 1:
        vol = input("Enter Volume number (1-32): ")
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print("\nGetting file...\nPlease wait")
    get_babel_text(hexagon, wall, shelf, vol)
    print("\nSuccessfully downloaded file!\nSearch in your current directory for a file named \"BabelBookOut.txt\"\n")

elif mode == "4":
    print("\nSelected Mode: Convert Manual into Automatic query\n")
    hexagon = input("Enter Hexagon name: ")
    while check_hex_isvalid(hexagon) == False or not hexagon:
        hexagon = input("\nEnter Hexagon name: ")
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    print(f"\nSelected Hexagon: {f"{hexagon[:10]}..." if len(hexagon) > 10 else hexagon}")
    
    wall = input("Enter Wall number (1-4): ")
    while not wall or not wall in string.digits or int(wall) > 4 or int(wall) < 1:
        wall = input("Enter Wall number (1-4): ")
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    print(f"\nSelected Hexagon: {f"{hexagon[:10]}..." if len(hexagon) > 10 else hexagon}")
    print(f"Selected Wall: {wall}")
    
    shelf = input("Enter Shelf number (1-5): ")
    while not shelf or not shelf in string.digits or int(shelf) > 5 or int(shelf) < 1:
        shelf = input("Enter Shelf number (1-5): ")
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    print(f"\nSelected Hexagon: {f"{hexagon[:10]}..." if len(hexagon) > 10 else hexagon}")
    print(f"Selected Wall: {wall}")
    print(f"Selected Shelf: {shelf}")
    
    vol = input("Enter Volume number (1-32): ")
    while not vol or check_vol_isvalid(vol) == False or int(vol) > 32 or int(vol) < 1:
        vol = input("Enter Volume number (1-32): ")
    if vol < 10:
        vol = f"0{vol}"
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    
    automatic_query = f"{hexagon}{wall}{shelf}{vol}"
    compressed_automatic_query = zlib.compress(automatic_query.encode())

    print(f"\nSelected Hexagon: {f"{hexagon[:10]}..." if len(hexagon) > 10 else hexagon}")
    print(f"Selected Wall: {wall}")
    print(f"Selected Shelf: {shelf}")
    print(f"Selected Volume: {vol}")
    print(f"\nAutomatic Query ID: {"Too long to display" if len(str(compressed_automatic_query)[2:-1]) > 30 else str(compressed_automatic_query)[2:-1]}")
    with open("AutoQueryOut.txt", "w") as write_auto_query_to_file:
        write_auto_query_to_file.write(str(compressed_automatic_query)[2:-1])
        print("\nWritten to output file\nSearch in your current directory for a file named \"AutoQueryOut.txt\"")

elif mode == "5":
    print("Exiting...")
    exit()

#Incorrect mode selected
else:
    print("No valid mode was selected")
