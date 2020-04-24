from spyre import server

import pandas as pd
import urllib
import json

from urllib import request

name='vhi_{}.csv'
df = pd.DataFrame()
for i in range(1, 26):
    temp = pd.read_csv(name.format(i), sep='[, ]+', engine='python')
    temp['Province'] = i
    df = df.append(temp, ignore_index=True)

class StockExample(server.App):
    title = "Historical Stock Prices"

    inputs = [{"type": 'dropdown',
               "label": 'Choose year',
               "options": [{'label': str(i), 'value': i} for i in range(1982, 2020)],
               'key': 'year',
               'value': '1982'},
                
                {
                    "type":'dropdown',
                    "label": 'Province',
                    "options" : [ {"label": "1", "value":"1"},
                                  {"label": "2", "value":"2"},
                                  {"label": "3", "value":"3"},
                                  {"label": "4", "value":"4"},
                                  {"label": "5", "value":"5"},
                                  {"label": "6", "value":"6"},
                                  {"label": "7", "value":"7"},
                                  {"label": "8", "value":"8"},
                                  {"label": "9", "value":"9"},
                                  {"label": "10", "value":"10"},
                                  {"label": "11", "value":"11"},
                                  {"label": "12", "value":"12"},
                                  {"label": "13", "value":"13"},
                                  {"label": "14", "value":"14"},
                                  {"label": "15", "value":"15"},
                                  {"label": "16", "value":"16"},
                                  {"label": "17", "value":"17"},
                                  {"label": "18", "value":"18"},
                                  {"label": "19", "value":"19"},
                                  {"label": "20", "value":"19"},
                                  {"label": "21", "value":"20"},
                                  {"label": "22", "value":"21"},
                                  {"label": "23", "value":"22"},
                                  {"label": "24", "value":"23"},
                                  {"label": "25", "value":"24"}],
                    "key": 'province',
                    "action_id": "update_data"
                },
                {
                    "type" : 'text',
                    "key" : 'min',
                    "label" : 'min',
                    "action_id" : 'simple_html_output'
                },
                {
                    "type" : 'text',
                    "key" : 'max',
                    "label" : 'max',
                    "action_id" : 'simple_html_output'
                }
                    
            ]

    outputs = [{'type': 'table',
                'id': 'table1',
                'control_id': 'apply',
                'tab': 'Table'},
               {'type': 'plot',
                'id': 'plot1',
                'control_id': 'apply',
                'tab': 'Plot'}]

    controls = [{"type": 'button',
                 'id': 'apply',
                 'label': 'Apply'}]

    tabs = ["Plot", "Table"]

    def getData(self, params):
        year = params['year']
        #province = params['Province']
        #min = params['min']
        #max = params['max']
        f = df[df['year'] == year].filter(['year', 'week', 'VHI', 'TCI', 'VCI'])
        #final = f[(f['week'] >= float(min)) & (f['week'] <= float(max))]
        #f['week'] = f['week'].astype(int)
        #f['week'] = f['week'].astype(str)
        return f

    def getPlot(self, params):
        df = self.getData(params)
        return df.set_index(df['week']).plot()

        
app = StockExample()
app.launch()
#нам нужно передать то, что ввел пользователь и потом вывести ряд для этих параметров
#