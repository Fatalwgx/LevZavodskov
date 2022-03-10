# Created by Lev Zavodskov
# Automated SQL comparator used to find discrepancies between two similar or supposedly identical tables, dbs.
# Note that this piece of code was edited to hide any confidential info AFTER I stopped working on the project this tool was made for. Therefore I have no means to test it and might have developed bugs
# that were not present in initial version of this tool. Anyway this representation should give you enough information about my skills. Ready to discuss your questions at any time.

import pandas as pd
import psycopg2 as pg
from configparser import ConfigParser
import time

#Connection credentials loaded from external config file
def connect_ppg2():
    try:
        conn = None
        with open('config.ini') as cf:
            parser = ConfigParser()
            parser.read_file(cf)
            conn = pg.connect(
                host=parser.get('connection', 'host'),
                database=parser.get('connection', 'database'),
                user=parser.get('connection', 'user'),
                password=parser.get('connection', 'password'),
                port=parser.get('connection', 'port')
            )
    except:
        print('Connection has failed') 
    return conn

#Outputs result from Postgres, extending max display rows in pandas. Was used for testing out dataframe output during development
def output_df():
    with pd.option_context('display.max_rows', None):
        print(df1)


#Connect to postgress, execute SQL query and store results in Dataframe
def create_df_from_ppg2(tname, tuniverse, exportversion,sw, conn):

    print('Executing SQL query & Saving to dataframe...', end='')
    
    #SQL query that will be performed on Postgres
    q = '''
    set schema 'qa';
    select legacy, redesign, id from (select l.id, l.'''+tname+''' as redesign, d.'''+tname+''' as legacy, (case when l.'''+tname+''' = d.'''+tname+''' then 1 when l.'''+tname+''' is null and d.'''+tname+''' is null then 2 else 0 end) as is_equal 
    from qa.redesignexport_'''+tuniverse+'''_'''+exportversion+''' l join qa.legacyexport_'''+tuniverse+'''_'''+exportversion+''' d on l.id = d.id where l.ends = \'''' +Date+ '''\' and d.ends = \'''' +Date+ '''\') as comp
    where is_equal = \''''+sw+'''\'
    order by id;
    '''
    return pd.read_sql_query(q, conn)

#Version
version = None
#Switches modes 0 will show discrepancies, 1 matches, 2 Null matches
switch = None
#Save Directory
save_dir = None
#Column names source
ColumnNamesSource = None
#Universe names source
UniverseNamesSource = None
#Date related filtering criteria
Date = None
#Current Date as String
today = time.strftime("%Y%m%d")

#Parses values from config.ini into the project
with open('config.ini') as cf:
    parser = ConfigParser()
    parser.read_file(cf)
    #Version
    version = parser.get('settings', 'version')
    #Switches modes 0 will show discrepancies, 1 matches, 2 Null matches
    switch = parser.get('settings', 'switch')
    #Save Directory
    save_dir = parser.get('settings', 'save_dir')
    #Column names source
    ColumnNamesSource = parser.get('settings', 'ColumnNamesSource')
    #Universe names source
    UniverseNamesSource = parser.get('settings', 'UniverseNamesSource')
    #Date
    Date = parser.get('settings', 'Date')

#Pulls input for column names
file1 = open(ColumnNamesSource, 'r')
Lines = file1.readlines()
file1.close()

#Pulls input for universe codes
file2 = open(UniverseNamesSource, 'r')
Universes = file2.readlines()
file2.close()


#Nested loop takes 1 universe runs through all of its specified columns and then switches to the next universe
for uni in Universes:
    univ = uni.strip('\n')
    MissedLog = []
    for line in Lines:
        #Fast and cheap way to catch errors with incorrect or non-existent column name. Code continues even after encountering an error.
        try:
            test_column = line.strip('\n')
            df1 = create_df_from_ppg2(test_column, univ, version, switch, connect_ppg2())
            print(univ +'...'+ test_column, end='...')
        except:
            print(univ+'...'+test_column+'...No such column in current universe')
            #Adds columns that were missed or encountered an error to a list
            MissedLog.append(test_column)
            continue

        #Cheap solution to compare float values with differenc acceptable tolerance points. Adds accuracy column to tables of float data type which outputs absolute discrepancy between two values. Can later be filtered during log review using excel
        if df1['leto'].dtypes == 'float64':
            for index, row in df1.iterrows():
                if row['leto'] != None and row['dbf'] != None or row['leto'] != 'nan' and row['dbf'] != 'nan' or row['leto'] != 'NoneType' and row['dbf'] != 'NoneType':
                    try:
                        df1.loc[index, 'accuracy'] = abs(row['leto'] - row['dbf'])
                    except:
                        pass

        #Skip to the next iteration if dataframe(table) is empty               
        if df1.empty:
            print('no discrepancy')
            continue
        
        #Saves dataframe(table) with discrepancies into a csv file
        df1.to_csv(save_dir+'\\'+today+'_'+univ.upper()+'_'+version+'_'+test_column+'_'+str(len(df1))+'.csv', sep = ',')
        print(str(len(df1)) +' logging')

    #Generates a log file containing column names that weren't present in tested universe or encountered somekind of error. Needs to be retested manually.
    with open(save_dir+'\\'+today + '_' + univ.upper() + '_' + version + '_MissedTables.txt', 'a') as f:
            for element in MissedLog:
                f.write(element+'\n')

#Prevents promt from closing immediately
print('Process Finished')
input('Press any key to exit')