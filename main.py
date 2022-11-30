"""
    Main function
"""
from data_quality import data_cleaning
from file_check import watcher
from output import output_

if __name__ == '__main__':
    file_ = watcher('test_folder',5)
    cleaned_df = data_cleaning(file_,'test_folder')
    output_(cleaned_df,'results')
