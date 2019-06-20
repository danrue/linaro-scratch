#!/usr/bin/python3

import json
import requests
import subprocess

key = subprocess.check_output("cat $HOME/.config/grafana_key", shell=True, encoding='utf-8').strip()

headers = {'Authorization': 'Bearer {}'.format(key)}
data = {
  "dashboard": {
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": "-- Grafana --",
        "enable": True,
        "hide": True,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "type": "dashboard"
      }
    ]
  },
  "description": "Linux Kernel Functional Testing",
  "editable": True,
  "gnetId": None,
  "graphTooltip": 0,
  "id": 2,
  "links": [],
  "panels": [
    {
      "cacheTimeout": None,
      "colorBackground": False,
      "colorPostfix": False,
      "colorPrefix": False,
      "colorValue": True,
      "colors": [
        "#299c46",
        "rgba(237, 129, 40, 0.89)",
        "#d44a3a"
      ],
      "format": "none",
      "gauge": {
        "maxValue": 100,
        "minValue": 0,
        "show": False,
        "thresholdLabels": False,
        "thresholdMarkers": True
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 0
      },
      "id": 9,
      "interval": None,
      "links": [],
      "mappingType": 1,
      "mappingTypes": [
        {
          "name": "value to text",
          "value": 1
        },
        {
          "name": "range to text",
          "value": 2
        }
      ],
      "maxDataPoints": 100,
      "NonePointMode": "connected",
      "NoneText": None,
      "postfix": "",
      "postfixFontSize": "50%",
      "prefix": "",
      "prefixFontSize": "50%",
      "rangeMaps": [
        {
          "from": "None",
          "text": "N/A",
          "to": "None"
        }
      ],
      "sparkline": {
        "fillColor": "rgba(31, 118, 189, 0.18)",
        "full": True,
        "lineColor": "rgb(31, 120, 193)",
        "show": True
      },
      "tableColumn": "",
      "targets": [
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tsum(core_projectstatus.tests_pass+core_projectstatus.tests_fail+core_projectstatus.tests_xfail) over (order by core_build.datetime) as lkft_test_count,\n\tcore_projectstatus.last_updated as \"time\"\nfrom\n\tcore_build\ninner join core_projectstatus on\n\tcore_projectstatus.build_id = core_build.id\nwhere\n\tcore_build.project_id IN (\n\tselect\n\t\tcore_project.id\n\tfrom\n\t\tcore_project\n\tinner join core_group on\n\t\tcore_group.id = core_project.group_id\n\twhere\n\t\tcore_group.slug = 'lkft'\n\torder by\n\t\tcore_project.id) and\n\t\tcore_projectstatus.last_updated is not None\norder by\n\tcore_projectstatus.last_updated;",
          "refId": "A",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        }
      ],
      "thresholds": "",
      "timeFrom": None,
      "timeShift": None,
      "title": "LKFT Tests Run",
      "type": "singlestat",
      "valueFontSize": "120%",
      "valueMaps": [
        {
          "op": "=",
          "text": "0",
          "value": "None"
        }
      ],
      "valueName": "max"
    },
    {
      "aliasColors": {},
      "bars": False,
      "cacheTimeout": None,
      "dashLength": 10,
      "dashes": False,
      "fill": 1,
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 0
      },
      "id": 11,
      "legend": {
        "avg": False,
        "current": True,
        "max": False,
        "min": False,
        "show": True,
        "total": False,
        "values": True
      },
      "lines": True,
      "linewidth": 1,
      "links": [],
      "NonePointMode": "None",
      "paceLength": 10,
      "percentage": False,
      "pointradius": 2,
      "points": False,
      "renderer": "flot",
      "seriesOverrides": [],
      "stack": False,
      "steppedLine": False,
      "targets": [
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tsum(core_projectstatus.tests_pass+core_projectstatus.tests_fail+core_projectstatus.tests_xfail) over (order by core_build.datetime) as lkft_test_count,\n\tsum(core_projectstatus.tests_pass) over (order by core_build.datetime) as lkft_test_pass_count,\n\tsum(core_projectstatus.tests_fail) over (order by core_build.datetime) as lkft_test_fail_count,\n\tsum(core_projectstatus.tests_xfail) over (order by core_build.datetime) as lkft_test_xfail_count,\n\tcore_projectstatus.last_updated as \"time\"\nfrom\n\tcore_build\ninner join core_projectstatus on\n\tcore_projectstatus.build_id = core_build.id\nwhere\n\tcore_build.project_id IN (\n\tselect\n\t\tcore_project.id\n\tfrom\n\t\tcore_project\n\tinner join core_group on\n\t\tcore_group.id = core_project.group_id\n\twhere\n\t\tcore_group.slug = 'lkft'\n\torder by\n\t\tcore_project.id) and\n\t\tcore_projectstatus.last_updated IS NOT None\norder by\n\tcore_projectstatus.last_updated;",
          "refId": "A",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        }
      ],
      "thresholds": [],
      "timeFrom": None,
      "timeRegions": [],
      "timeShift": None,
      "title": "LKFT Tests Run",
      "tooltip": {
        "shared": True,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "buckets": None,
        "mode": "time",
        "name": None,
        "show": True,
        "values": []
      },
      "yaxes": [
        {
          "format": "short",
          "label": None,
          "logBase": 1,
          "max": None,
          "min": None,
          "show": True
        },
        {
          "format": "short",
          "label": None,
          "logBase": 1,
          "max": None,
          "min": None,
          "show": True
        }
      ],
      "yaxis": {
        "align": False,
        "alignLevel": None
      }
    },
    {
      "aliasColors": {},
      "bars": False,
      "dashLength": 10,
      "dashes": False,
      "datasource": "qa-reports",
      "fill": 1,
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 8
      },
      "hideTimeOverride": False,
      "id": 4,
      "legend": {
        "avg": False,
        "current": False,
        "max": False,
        "min": False,
        "show": True,
        "total": False,
        "values": False
      },
      "lines": True,
      "linewidth": 1,
      "links": [],
      "NonePointMode": "None",
      "paceLength": 10,
      "percentage": False,
      "pointradius": 2,
      "points": False,
      "renderer": "flot",
      "seriesOverrides": [],
      "stack": False,
      "steppedLine": False,
      "targets": [
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tnext.tests_pass as next_pass_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as next on next.build_id = b.id\nwhere\n\tb.project_id = 6 and next.tests_pass>100\norder by\n\tb.datetime;",
          "refId": "G",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        },
        {
          "format": "time_series",
          "group": [
            {
              "params": [
                "$__interval",
                "none"
              ],
              "type": "time"
            }
          ],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tmainline.tests_pass as mainline_pass_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as mainline on mainline.build_id = b.id\nwhere\n\tb.project_id = 22 and mainline.tests_pass>100\norder by\n\tb.datetime;",
          "refId": "A",
          "select": [
            [
              {
                "params": [
                  "id"
                ],
                "type": "column"
              },
              {
                "params": [
                  "count"
                ],
                "type": "aggregate"
              },
              {
                "params": [
                  "id"
                ],
                "type": "alias"
              }
            ]
          ],
          "table": "core_test",
          "timeColumn": "test_run_id",
          "timeColumnType": "int4",
          "where": [
            {
              "name": "$__unixEpochFilter",
              "params": [],
              "type": "macro"
            }
          ]
        },
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tstable_5_1.tests_pass as stable_5_1_pass_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as stable_5_1 on stable_5_1.build_id = b.id\nwhere\n\tb.project_id = 167 and stable_5_1.tests_pass>100\norder by\n\tb.datetime;",
          "refId": "F",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        },
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tstable_4_14.tests_pass as stable_4_14_pass_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as stable_4_14 on stable_4_14.build_id = b.id\nwhere\n\tb.project_id = 58 and stable_4_14.tests_pass>100\norder by\n\tb.datetime;",
          "refId": "E",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        },
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tstable_4_19.tests_pass as stable_4_19_pass_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as stable_4_19 on stable_4_19.build_id = b.id\nwhere\n\tb.project_id = 135 and stable_4_19.tests_pass>100\norder by\n\tb.datetime;\n  ",
          "refId": "C",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        },
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tstable_4_9.tests_pass as stable_4_9_pass_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as stable_4_9 on stable_4_9.build_id = b.id\nwhere\n\tb.project_id = 23 and stable_4_9.tests_pass>100\norder by\n\tb.datetime;\n  ",
          "refId": "B",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        },
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tstable_4_4.tests_pass as stable_4_4_pass_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as stable_4_4 on stable_4_4.build_id = b.id\nwhere\n\tb.project_id = 40 and stable_4_4.tests_pass>100\norder by\n\tb.datetime;",
          "refId": "D",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        }
      ],
      "thresholds": [],
      "timeFrom": None,
      "timeRegions": [],
      "timeShift": None,
      "title": "Test Pass Counts Per Branch",
      "tooltip": {
        "shared": True,
        "sort": 0,
        "value_type": "individual"
      },
      "transparent": True,
      "type": "graph",
      "xaxis": {
        "buckets": None,
        "mode": "time",
        "name": None,
        "show": True,
        "values": []
      },
      "yaxes": [
        {
          "format": "short",
          "label": None,
          "logBase": 1,
          "max": None,
          "min": None,
          "show": True
        },
        {
          "format": "short",
          "label": None,
          "logBase": 1,
          "max": None,
          "min": None,
          "show": True
        }
      ],
      "yaxis": {
        "align": False,
        "alignLevel": None
      }
    },
    {
      "aliasColors": {},
      "bars": False,
      "dashLength": 10,
      "dashes": False,
      "datasource": "qa-reports",
      "fill": 1,
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 8
      },
      "hideTimeOverride": False,
      "id": 7,
      "legend": {
        "avg": False,
        "current": False,
        "max": False,
        "min": False,
        "show": True,
        "total": False,
        "values": False
      },
      "lines": True,
      "linewidth": 1,
      "links": [],
      "NonePointMode": "None",
      "paceLength": 10,
      "percentage": False,
      "pointradius": 2,
      "points": False,
      "renderer": "flot",
      "seriesOverrides": [],
      "stack": False,
      "steppedLine": False,
      "targets": [
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tnext.tests_fail as next_fail_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as next on next.build_id = b.id\nwhere\n\tb.project_id = 6\norder by\n\tb.datetime;",
          "refId": "G",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        },
        {
          "format": "time_series",
          "group": [
            {
              "params": [
                "$__interval",
                "none"
              ],
              "type": "time"
            }
          ],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tmainline.tests_fail as mainline_fail_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as mainline on mainline.build_id = b.id\nwhere\n\tb.project_id = 22\norder by\n\tb.datetime;",
          "refId": "A",
          "select": [
            [
              {
                "params": [
                  "id"
                ],
                "type": "column"
              },
              {
                "params": [
                  "count"
                ],
                "type": "aggregate"
              },
              {
                "params": [
                  "id"
                ],
                "type": "alias"
              }
            ]
          ],
          "table": "core_test",
          "timeColumn": "test_run_id",
          "timeColumnType": "int4",
          "where": [
            {
              "name": "$__unixEpochFilter",
              "params": [],
              "type": "macro"
            }
          ]
        },
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tstable_5_1.tests_fail as stable_5_1_fail_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as stable_5_1 on stable_5_1.build_id = b.id\nwhere\n\tb.project_id = 167\norder by\n\tb.datetime;",
          "refId": "F",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        },
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tstable_4_14.tests_fail as stable_4_14_fail_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as stable_4_14 on stable_4_14.build_id = b.id\nwhere\n\tb.project_id = 58\norder by\n\tb.datetime;",
          "refId": "E",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        },
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tstable_4_19.tests_fail as stable_4_19_fail_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as stable_4_19 on stable_4_19.build_id = b.id\nwhere\n\tb.project_id = 135\norder by\n\tb.datetime;\n  ",
          "refId": "C",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        },
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tstable_4_9.tests_fail as stable_4_9_fail_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as stable_4_9 on stable_4_9.build_id = b.id\nwhere\n\tb.project_id = 23\norder by\n\tb.datetime;\n  ",
          "refId": "B",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        },
        {
          "format": "time_series",
          "group": [],
          "metricColumn": "none",
          "rawQuery": True,
          "rawSql": "select\n\tstable_4_4.tests_fail as stable_4_4_fail_count,\n\tb.datetime as \"time\"\nfrom\n\tcore_build as b\ninner join core_projectstatus as stable_4_4 on stable_4_4.build_id = b.id\nwhere\n\tb.project_id = 40\norder by\n\tb.datetime;",
          "refId": "D",
          "select": [
            [
              {
                "params": [
                  "metrics_summary"
                ],
                "type": "column"
              }
            ]
          ],
          "table": "core_projectstatus",
          "timeColumn": "created_at",
          "timeColumnType": "timestamp",
          "where": [
            {
              "name": "$__timeFilter",
              "params": [],
              "type": "macro"
            }
          ]
        }
      ],
      "thresholds": [],
      "timeFrom": None,
      "timeRegions": [],
      "timeShift": None,
      "title": "Test Fail Counts Per Branch",
      "tooltip": {
        "shared": True,
        "sort": 0,
        "value_type": "individual"
      },
      "transparent": True,
      "type": "graph",
      "xaxis": {
        "buckets": None,
        "mode": "time",
        "name": None,
        "show": True,
        "values": []
      },
      "yaxes": [
        {
          "format": "short",
          "label": None,
          "logBase": 1,
          "max": None,
          "min": None,
          "show": True
        },
        {
          "format": "short",
          "label": None,
          "logBase": 1,
          "max": None,
          "min": None,
          "show": True
        }
      ],
      "yaxis": {
        "align": False,
        "alignLevel": None
      }
    }
  ],
  "schemaVersion": 18,
  "style": "dark",
  "tags": [],
  "templating": {
    "list": []
  },
  "time": {
    "from": "now-6h",
    "to": "now"
  },
  "timepicker": {
    "refresh_intervals": [
      "5s",
      "10s",
      "30s",
      "1m",
      "5m",
      "15m",
      "30m",
      "1h",
      "2h",
      "1d"
    ],
    "time_options": [
      "5m",
      "15m",
      "1h",
      "6h",
      "12h",
      "24h",
      "2d",
      "7d",
      "30d"
    ]
  },
  "timezone": "",
  "title": "LKFT",
  "uid": "2co7gfmZk",
  "version": 12
},
  "expires": 3600,
  "external": True,
  "key": "zxcvzxcv",
  "deleteKey": "asdfasdf",
  "name": "qwerqwre",
}
#r = requests.post('https://httpbin.org/post', data = json.dumps(data), headers = headers)
r = requests.post('https://grafana.linaro.org/api/snapshots', json = data, headers = headers)
print(r)
print(r.text)

