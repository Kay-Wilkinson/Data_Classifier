import csv, re, random, string
from .tests import regex_string_test
from .experimental import iab_deep_search

'''
Open input CSV file and convert into an ordered dictionary
'''
def read_and_parse_target(file_name):
    with open(file_name, 'r') as input_file:
        csv_reader = csv.DictReader(input_file)
        x = list()
        for row in csv_reader:
            tags = row['tag_name'].lower()
            x.append(tags)
        dict_tags = {tag:0 for tag in x}
        return dict_tags

'''
Search in dictionary of Tags
'''
def reg_check_male_and_female(dict_tags):
    regex_list = ['female', '_female', 'lady', 'ladies', 'women', 'male', 'males', '_male']

    regex_list_compiled = [re.compile(i) for i in regex_list]
    matched_tags_dict = {k:v for k,v in dict_tags.items() if any (re.match(regex,k) for regex in regex_list_compiled)}

    regex_lookahead_compiled = [re.compile("(" + i + ")") for i in regex_list]
    matched_tags_dict_2 = {k: v for k, v in dict_tags.items() if any(re.findall(regex, k) for regex in regex_lookahead_compiled)}

    return matched_tags_dict, matched_tags_dict_2


def reg_check_age(dict_tags):
    regex_age_list = ['\d', '([0-9])']
    regex_age_list_compiled = [re.compile(i) for i in regex_age_list]

    matched_age_tags_dict = {k: v for k, v in dict_tags.items() if any(re.match(regex, k) for regex in regex_age_list_compiled)}
    findall_dict = {k: v for k, v in dict_tags.items() if any(re.findall(regex, k) for regex in regex_age_list_compiled)}

    return matched_age_tags_dict, findall_dict


def reg_check_gender(dict_tags):
    regex_gender_list = ['gender']
    regex_gender_list_compiled = [re.compile(i) for i in regex_gender_list]

    matched_gender_tags_dict = {k: v for k, v in dict_tags.items() if any(re.match(regex, k) for regex in regex_gender_list_compiled)}
    findall_dict = {k: v for k, v in dict_tags.items() if any(re.findall(regex, k) for regex in regex_gender_list_compiled)}

    return matched_gender_tags_dict, findall_dict

'''
Search & remove edge case matches
'''
def edge_case_check(input):
    '''
    This is to find and delete cases e.g. $4000 and 1st
    '''
    edge_case_list = ['([0-9]+st)', '([0-9]+nd)', '([0-9]+th)', '(\$+[0-9])']
    edge_case_list_compiled = [re.compile(i) for i in edge_case_list]

    found_edge_cases = {k: v for k, v in input.items() if any(re.findall(regex, k) for regex in edge_case_list_compiled)}
    new_dict = {input:found_edge_cases[input] for input.keys() in input.keys() if input.keys()!=found_edge_cases}

    return new_dict

'''
Write cached dictionaries to csv
'''
def dictionaries_to_csv(male_dict, female_dict, age_dict, misc_dict):

    def randomString(stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))
    file_name = 'classified_inge_tag_list_{}.csv'.format(randomString(5))
    print(file_name)
    with open(file_name, 'w') as output_file:
        fieldnames = ['Category - Women', 'Category - Men', 'Category - Age', 'Category - Misc']
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()
        for m in male_dict:
            csv_writer.writerow(m)
        for f in female_dict:
            csv_writer.writerow(f)
        for a in age_dict:
            csv_writer.writerow(a)
        for g in misc_dict:
            csv_writer.writerow(g)

if __name__ == '__main__':

    tags = read_and_parse_target('inge_tag_list.csv')

    mf_d_0, mf_d_1 = reg_check_male_and_female(tags)
    a_d = reg_check_age(tags)
    g_d = reg_check_gender(tags)

    e_d = edge_case_check(a_d)

    dictionaries_to_csv(mf_d_0, mf_d_1, a_d, e_d)

    # regex string tests to be sure that my broken code is not me finally going crazy
    regex_test = r"([0-9])"
    string_test = "'a25-49 (nbcu)'"
    regex_string_test.reg_test(regex_test, string_test)