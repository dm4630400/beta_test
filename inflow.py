import datetime,xlrd,openpyxl
basepath = "D:\\PYTHON\\"
today = datetime.date.today()
yesterday = (today - datetime.timedelta(days=1)).strftime('%d')
d, m = datetime.datetime.today().strftime('%d'), datetime.datetime.today().strftime('%m')
file_inflow = f"{basepath}MUR_SUBS_INFLOW_2020_{m}_{yesterday}.xlsx"
print(file_inflow)
book=xlrd.open_workbook(file_inflow)
sheet=book.sheet_by_index(0)
num_rows,num_col=sheet.nrows,sheet.ncols
print(num_rows,num_col)
list_of_dates = {}

for rownum in range(sheet.nrows):
    rv = sheet.row_values(rownum)
    twn,act,tec,nls,subs_id = rv[32],rv[26],rv[13],rv[4],rv[85]
    if twn == 'Город Апатиты' and (tec in ['PON','FTTx']):
        list_of_dates[act] = [tec,nls,subs_id]

file_report = f"{basepath}report_inflow_{m}.xlsx"
wb_report = openpyxl.load_workbook(file_report, read_only=False)
ws_report = wb_report.active

for i,k in enumerate(sorted(list_of_dates.keys())):
    shift = str(i+2)
    ws_report["A"+shift] = k
    ws_report["B"+shift] = "ЛТУ г.Апатиты"
    ws_report["C"+shift] = list_of_dates[k][0] #tec
    ws_report["D"+shift] = list_of_dates[k][1] #nls
    ws_report["P"+shift] = list_of_dates[k][2] #subs_id
wb_report.save(str(file_report))
