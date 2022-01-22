# general
import numpy as np
import pandas as pd

# define function to sum 2 numbers
def sum_two_numbers(val_1, val_2):
    # get sum
    val_sum = val_1 + val_2
    # return val_sum
    return val_sum

# define function to sum list
def sum_list(list_vals):
    # get sum
    val_sum = np.sum(list_vals)
    # print
    print(f'The sum of {len(list_vals)} values is {val_sum}')
    # return
    return val_sum

# class for data frame operations
class DataFrameOps:
    # init
    def __init__(self):
        pass
    # function that reads in a csv
    def read_csv_file(self, str_filepath):
        # read csv
        df = pd.read_csv(str_filepath)
        # print message
        print(f'Data frame successfully imported from {str_filepath}')
        # save df to object
        self.df = df
        # return
        return self
    # function that multiplies 2 columns
    def multiply_two_cols(self, str_col1, str_col2):
        # multiply columns
        self.df[f'{str_col1}_x_{str_col2}'] = self.df[str_col1] * self.df[str_col2]
        # return
        return self
