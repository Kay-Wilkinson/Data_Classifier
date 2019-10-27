def format_load_query(file_name, table_name):
    sql_query = f"""
                LOAD DATA LOCAL INFILE '{file_name}' 
                INTO TABLE {table_name}\
                FIELDS TERMINATED BY ',' 
                ENCLOSED BY '"' 
                IGNORE 1 LINES;
                """
    return sql_query


def format_select_query(table_name):
    sql_query = f"""
                SELECT * 
                FROM {table_name}
                """
    return sql_query