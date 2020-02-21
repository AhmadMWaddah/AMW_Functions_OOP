import numpy as np  # For Matrices Manipulations
import pandas as pd  # For Data frames etc
import xlrd  # For Excel Files
import os  # For Changing to the Correct Directory


# -------------------- #
class CharacterFind:
    def __init__(self, func):
        self.func = func

    @property
    def __call__(self):
        return self.func()


@CharacterFind
def character_find(target_string, icon_symbol):
    """
    Custom Function Takes 2 Parameters String and Symbol and Find Where This Symbol and How Many in Target.

    :param target_string: to loop inside and look for symbol
    :param icon_symbol: will look for it inside that target
    :return: count how many times symbol found in the target.

    """
    # Start Counting Variable.
    count_starter = 0
    # List To Append Symbol Each Time Found In String.
    target_list = []
    # Looping In String For Symbol.
    for character in target_string:
        if character.lower() == icon_symbol.lower():
            # Append Symbol To List To Count It.
            target_list.append(target_string.find(character, count_starter))
        # Add One For Starter To Skip Previous Character.
        count_starter += 1
    # Printing The List With Symbol Positions On String (Target).
    print(target_list)


# -------------------- #
class CustomSplit:
    def __init__(self, split_func):
        self.split_func = split_func

    @property
    def __call__(self):
        return self.split_func()


@CustomSplit
def custom_split(target_string):
    """
    Function Take One Parameter a an iterable object and loop and split it for parts and append it to a list.
    :param target_string: iterable object
    :return: List with splited part of iterable.

    """
    # List To Append All Splited Words.
    splited_words_list = []
    # Variable To Save Words.
    helper_variable = ''
    # Looping Inside String.
    for each_word in target_string:
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


# -------------------- #
class RenameFiles:
    def __init__(self, rename_func):
        self.rename_func = rename_func

    @property
    def __call__(self):
        return self.rename_func()

@RenameFiles
def rename_files(files_path, wanted_name, needed_extension):
    """
    Function Takes 3 Parameters Files Directory and Name for files we need it to be and extension of the files.

    :param files_path: Folder that files inside.
    :param wanted_name: the name we need to rename the files with.
    :param needed_extension: the new extension for the files we need to rename it.
    :return: List with the new named Files.

    """
    # List For All Files In Directory.
    directory_files = []
    # New List After Renaming Files.
    renamed_files = []
    # Numerical Range To Give To Files.
    numbering_list = range(0, 6)
    # Looping Inside Directory.
    for filename in os.listdir(files_path):
        # Adding Each File As Member In Directory Files List.
        directory_files.append(filename)
    print(directory_files)

    # Looping For Two Lists, (Directory Files List and Numerical List).
    for each_file, each_number in zip(directory_files, numbering_list):
        # Creating Pattern For The New Name.
        new_name = f'{wanted_name} {each_number}.{needed_extension}'
        # Adding New Names To New List (Renamed List).
        renamed_files.append(new_name)
    # Printing List With New Names.
    print(renamed_files)


# Statistics Functions.
# -------------------- #
class MeanSquareError:
    def __init__(self, MSE_func):
        self.MSE_func = MSE_func

    @property
    def __call__(self):
        return self.MSE_func()

@MeanSquareError
# Mean Squared Error.
def mean_square_error(actual_data, predicted_data):
    """
    Function Takes 2 Parameters lists of data, making counter and add to it and zipping lists.
    :param actual_data:
    :param predicted_data:
    :return: Mean Squared Error Of Both Data Actual and Predicted.

    """
    # Starter Counter.
    counter = 0
    # Combining BOth List With Zipping Function.
    data_combined = zip(actual_data, predicted_data)
    # Loop For Each cell in both data.
    for (each_actual, each_predicted) in data_combined:
        # Adding Results To Starter Counter.
        counter += (each_actual - each_predicted) ** 2
    return counter / len(actual_data)


# -------------------- #
class MeanData:
    def __init__(self, mean_func):
        self.mean_func = mean_func

    @property
    def __call__(self):
        return self.mean_func()

@MeanData
def data_mean(data_values):
    """
    Getting The Mean Number For Data.
    :param data_values: Set Of Data
    :return: Mean Of Data Values.
    """
    return sum(data_values) / len(data_values)


# -------------------- #
class VarianceData:
    def __init__(self, variance_func):
        self.variance_func = variance_func

    @property
    def __call__(self):
        return self.variance_func()

@VarianceData
def data_variance(data_values, mean_of_data):
    """
    Getting The Variance Number For Data.
    :param data_values: Set Of Data
    :param mean_of_data: Mean Of Data From Previous Function.
    :return: Variance Of Data.
    """
    starter_counter = 0
    for data_cells in data_values:
        starter_counter += (data_cells - mean_of_data) ** 2
    return starter_counter / len(data_values)


# -------------------- #
class CoVarianceData:
    def __init__(self, covariance_func):
        self.covariance_func = covariance_func

    @property
    def __call__(self):
        return self.covariance_func()

@CoVarianceData
def data_covariance(features_values, labels_values, features_mean, labels_mean):
    """
    It measures the degree of change in the variables, i.e. when one variable changes, will there be the same/a similar change in the other variable.
    :param features_values: (X) Weights and Features Of Data
    :param labels_values: (Y) Predictions and Labels Of Data
    :param features_mean: Measured Mean Of Features For Data
    :param labels_mean: Measured Mean Of Labels For Data
    :return: Measure of relationship between 2 variables.

    """
    # Labels and Features Added and Multiplied.
    features_labels_sum_multiply = 0
    # Combine Both Features and Labels In One Object.
    feature_label_combined = zip(features_values, labels_values)
    for (features_values, labels_values) in feature_label_combined:
        features_labels_sum_multiply += ((features_values - features_mean) * (labels_values - labels_mean))
    return features_labels_sum_multiply / len(features_values)


# -------------------- #
class CoEfficientData:
    def __init__(self, coefficient_func):
        self.coefficient_func = coefficient_func

    @property
    def __call__(self):
        return self.coefficient_func()

@CoEfficientData
def data_coefficient(features_values, labels_values):
    """
    Measure of correlation overcomes the scale dependency of covariance by standardizing the measures.
    :param features_values: (X) Weights and Features Of Data
    :param labels_values: (Y) Predictions and Labels Of Data
    :return: Number Between 0 and 1.

    """
    features_mean = data_mean(features_values)
    labels_values = data_mean(labels_values)
    features_variance = data_variance(features_values, features_mean)
    labels_variance = data_variance(labels_values, labels_values)
    print(features_variance)
    beta_one = data_covariance(features_values, labels_values, features_mean, labels_values) / features_variance
    beta_zero = labels_values - (beta_one * features_mean)
    return beta_one, beta_zero


# -------------------- #
class SimpleLinearRegression:
    def __init__(self, spl_func):
        self.spl_func = spl_func

    @property
    def __call__(self):
        return self.spl_func()

@SimpleLinearRegression
def simple_linear_regression(features_train, labels_train, features_test):
    """
    Using a linear regression model will allow you to discover whether a relationship between variables exists at all.
    :param features_train:
    :param labels_train:
    :param features_test:
    :return:
    """
    beta_one_train, beta_zero_train = data_coefficient(features_train, labels_train)
    predicted_data = beta_one_train * features_test + beta_zero_train
    return predicted_data


# -------------------- #
class EvaluateModel:
    def __init__(self, eval_func):
        self.eval_func = eval_func

    @property
    def __call__(self):
        return self.eval_func()

@EvaluateModel
def evaluate_model(features_train, labels_train, features_test, labels_test):
    """
    Evaluate Model anc Compare Train Data With Test Data.
    :param features_train:
    :param labels_train:
    :param features_test:
    :param labels_test:
    :return:
    """
    prediction_data = simple_linear_regression(features_train, labels_train, features_test)
    return mean_square_error(prediction_data, labels_test)
