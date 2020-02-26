import os

# --------------------------------------------------- #
class CharacterFind:
    def __init__(self, target_string, icon_symbol):
        """
        :param target_string:       Provided String To Search Inside.
        :param icon_symbol:         Character Search For Inside String
        :return:    ---------->     How Many Times Repeated The Character and Indexes Too.
        """
        self.target_string = target_string
        self.icon_symbol = icon_symbol

    def character_find(self):
        # Start Counting Variable.
        count_starter = 0
        # List To Append Symbol Each Time Found In String.
        target_list = []
        # Looping In String For Symbol.
        for character in self.target_string:
            if character.lower() == self.icon_symbol.lower():
                # Append Symbol To List To Count It.
                target_list.append(self.target_string.find(character, count_starter))
            # Add One For Starter To Skip Previous Character.
            count_starter += 1
        # Printing The List With Symbol Positions On String (Target).
        repeated_times = len(target_list)
        print(target_list, repeated_times)
        return target_list, repeated_times

# --------------------------------------------------- #

class CustomSplit:
    def __init__(self, provided_string):
        """
        :param provided_string:     String To Loop Inside & Split Words.
        :return:    ----------->    Splited Words In a List.
        """
        self.provided_string = provided_string

    def custom_split(self):

        # List To Append All Splited Words.
        splited_words_list = []
        # Variable To Save Words.
        helper_variable = ''
        # Looping Inside String.
        for each_word in self.provided_string:
            # checking the next character is space or not.
            if each_word == ' ':
                # If Yes. Append Word To List.
                splited_words_list.append(helper_variable)
                # Then Reset Temporary Variable
                helper_variable = ''
            else:
                # If Not Then Fill Variable With Word.
                helper_variable += each_word

        # Last Word Will Be Out Of Loop Then Go To List Right Away.
        if helper_variable:
            splited_words_list.append(helper_variable)

        print(splited_words_list)
        return splited_words_list

# --------------------------------------------------- #

class RenameFiles:
    def __init__(self, files_path, wanted_name, count_of_files, needed_extension):
        """
        :param files_path:               Directory To Rename Files Inside
        :param wanted_name:              New Name To Rename Into.
        :param count_of_files:           How Many File To Be Renamed
        :param needed_extension:         Directory, Also, Wanted Name, & Extension.
        """
        self.files_path = files_path
        self.wanted_name = wanted_name
        self.needed_extension = needed_extension
        self.count_of_files = count_of_files

    def rename_files(self):
        # List For All Files In Directory.
        directory_files = []
        # New List After Renaming Files.
        renamed_files = []
        # Numerical Range To Give To Files.
        numbering_list = range(1, self.count_of_files + 1)
        # Looping Inside Directory.
        for filename in os.listdir(self.files_path):
            # Adding Each File As Member In Directory Files List.
            directory_files.append(filename)
        print(directory_files)

        # Looping For Two Lists, (Directory Files List and Numerical List).
        for each_file, each_number in zip(directory_files, numbering_list):
            # Creating Pattern For The New Name.
            new_name = f'{self.wanted_name} ({each_number}).{self.needed_extension}'
            # Adding New Names To New List (Renamed List).
            renamed_files.append(new_name)
        # Printing List With New Names.
        print(renamed_files)
        return renamed_files
