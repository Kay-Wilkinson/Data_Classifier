import csv, re, random, string
from tests import regex_string_test
# from .experimental import iab_deep_search

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
def reg_check_male(dict_tags):
    regex_list = ['male', 'males', '_male']

    regex_list_compiled = [re.compile(i) for i in regex_list]
    matched_tags_dict = {k:v for k,v in dict_tags.items() if any (re.match(regex,k)
                                                                  for regex in regex_list_compiled)}

    regex_lookahead_compiled = [re.compile("(" + i + ")") for i in regex_list]
    matched_tags_dict_2 = {k: v for k, v in dict_tags.items() if any(re.findall(regex, k)
                                                                     for regex in regex_lookahead_compiled)}

    output_dict = {**matched_tags_dict, **matched_tags_dict_2}
    return output_dict


def reg_check_female(dict_tags):
    regex_list = ['female', '_female', 'lady', 'ladies', 'women']

    regex_list_compiled = [re.compile(i) for i in regex_list]
    matched_tags_dict = {k:v for k,v in dict_tags.items() if any (re.match(regex,k)
                                                                  for regex in regex_list_compiled)}

    regex_lookahead_compiled = [re.compile("(" + i + ")") for i in regex_list]
    matched_tags_dict_2 = {k: v for k, v in dict_tags.items() if any(re.findall(regex, k)
                                                                     for regex in regex_lookahead_compiled)}

    output_dict = {**matched_tags_dict, **matched_tags_dict_2}
    return output_dict


def reg_check_age(dict_tags):
    regex_age_list = ['\d', '([0-9])']
    regex_age_list_compiled = [re.compile(i) for i in regex_age_list]

    matched_age_tags_dict = {k: v for k, v in dict_tags.items() if any(re.match(regex, k)
                                                                       for regex in regex_age_list_compiled)}
    findall_dict = {k: v for k, v in dict_tags.items() if any(re.findall(regex, k)
                                                              for regex in regex_age_list_compiled)}

    output_dict = {**matched_age_tags_dict, **findall_dict}
    return output_dict


def reg_check_gender(dict_tags):
    regex_gender_list = ['gender']
    regex_gender_list_compiled = [re.compile(i) for i in regex_gender_list]

    matched_gender_tags_dict = {k: v for k, v in dict_tags.items() if any(re.match(regex, k)
                                                                          for regex in regex_gender_list_compiled)}
    findall_dict = {k: v for k, v in dict_tags.items() if any(re.findall(regex, k)
                                                              for regex in regex_gender_list_compiled)}

    output_dict = {**matched_gender_tags_dict, **findall_dict}
    return output_dict


def edge_case_check(dicty_boi):
    '''
    These will output to a seperate column, it is up to you to decision on them.
    I did not delete them, in case there was overlap and you needed to keep some, e.g.:
    "rtl nl - gender & age - female 20-34 [1st & 3rd party - extend]" shouldn't be deleted as it is
    a female and age tag, despite having 1st and 3rd in it.
    '''
    input_0 = dicty_boi

    edge_case_list = ['([0-9]+st)', '([0-9]+nd)', '([0-9]+rd)', '([0-9]+th)', '(\$+[0-9])']
    edge_case_list_compiled = [re.compile(i) for i in edge_case_list]

    found_edge_cases = {k: v for k, v in input_0.items() if any(re.findall(regex, k)
                                                                for regex in edge_case_list_compiled)}

    return found_edge_cases

'''
Write cached dictionaries to csv
'''
def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(stringLength))


def dict_to_listed_csv(male_dict, female_dict, age_dict, misc_dict, edge_case_dict, file_name):
    final_results = []
    final_results.append(tuple([k for k in male_dict.keys()]))
    final_results.append(tuple([k for k in female_dict.keys()]))
    final_results.append(tuple([k for k in age_dict.keys()]))
    final_results.append(tuple([k for k in misc_dict.keys()]))
    final_results.append(tuple([k for k in edge_case_dict.keys()]))

    with open(file_name, 'w') as output_file:
        headers = ['Category - Men',
                   'Category - Female',
                   'Category - Age',
                   'Category - Misc', 
                   'Edge Cases - Delete Post-Perligo']
        rows = [headers]
        for data in final_results:
            rows.append(data)
        writer = csv.writer(output_file)
        writer.writerows(rows)


if __name__ == '__main__':
    # Read from CSV
    tags = read_and_parse_target('inge_tag_list.csv')
    # Compare tag categories against Regex compilation
    m = reg_check_male(tags)
    f = reg_check_female(tags)
    a = reg_check_age(tags)
    g = reg_check_gender(tags)
    edge = edge_case_check(tags)
    # Generate unique file name to write to
    write_file_name = 'classified_inge_tag_list_{}.csv'.format(random_string(5))
    # Write each tag category to a list of tuples. Write that to a csv file
    dict_to_listed_csv(m, f, a, g, edge, write_file_name)
    '''
    Regex String Tests
    '''
    regex_test = r"([0-9])"
    string_test = "'a25-49 (nbcu)'"
    # test_1 = regex_string_test.reg_test(regex_test, string_test)