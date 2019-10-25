# greenSourceBackend
![db](https://raw.githubusercontent.com/RRua/greenSourceBackend/master/greenRepo/db_schema.png)

# GreenSource
####python manage.py makemigrations
####python manage.py migrate
####python manage.py runserver


## NOTES
### Metrics coeficient refers the factor relative to the IS (International System) units ( 1 second -> coeficient 1, 13 ms -> coeficient = 0.001)


```
## API

- AndroidProject
  - [GET  /projects/] 
  - [POST /projects/]
  - [GET  /projects/<project_id>/]

- Application
  - [GET /apps/](#get-apps)
  - [POST /apps/](#post-apps)
  - [GET /apps/permissions/](#get-permissions)
  - [POST /apps/permissions/](#post-permissions)
  - [GET /apps/<app_id>/](#get-app)
  - [POST /apps/<app_id>/](#post-app)
  - [GET /apps/<app_id>/tests/](#app-tests)
  - [POST /apps/<app_id>/tests/](#app-tests)
  - [GET /apps/<app_id>/results/](#app-results)
  - [POST /apps/<app_id>/results/](#app-results)
  - [GET /apps/<app_id>/classes/](#app-classes)
  - [POST /apps/<app_id>/classes/](#app-classes)
  - [GET /apps/<app_id>/methods/](#app-methods)
  - [POST /apps/<app_id>/methods/](#app-methods)
  - [GET /apps/<app_id>/methods/<method_id>/](#app-method)
  - [POST /apps/<app_id>/methods/<method_id>/](#app-method)
  - [GET /apps/metrics/](#app-metrics)
  - [POST /apps/metrics/](#app-metrics)

- Class
  - [GET /apps/<app_id>/classes/](#get-class)
  - [POST /apps/<app_id>/classes/](#post-class)
  - [GET /classes/](#get-classes)
  - [POST /classes/](#post-classes)
  - [GET /classes/metrics/](#class-metrics)
  - [POST /classes/metrics/](#class-metrics)

- Method
  - [GET /apps/<app_id>/methods/](#app-methods)
  - [POST /apps/<app_id>/methods/](#app-methods)
  - [GET /methods/](#methods)
  - [POST /methods/](#methods)
  - [GET /methods/metrics/](#methods-metrics)
  - [POST /methods/metrics/](#methods-metrics)

- Test 
  - [GET /tests/](#app-tests)
  - [POST /tests/](#app-tests)
  - [GET /tests/<test_id>/results/](#test-results)
  - [POST /tests/<test_id>/results/](#test-results)
  - [GET /tests/metrics/](#app-tests)
  - [POST /tests/metrics/](#app-tests)

- Device
  - [GET /devices/](#devices)
  - [POST /devices/](#devices)

- Result
  - [GET /results/](#results)
  - [POST /results/](#results)

---




```

### POST /populate/
Povoa a BD com metricas, tools e dados relevantes.

### POST /populateTest/
Povoa a BD com dados dummy para fins de testing.

### GET /projects/
#### Response (CODE HTTP200)
```json
[
	{
	      "project_id": "2bb46be6-f071-413d-9221-c090a8f0cb29",
	      "project_build_tool": "gradle",
	      "project_desc": ""
    },
    {
	      "project_id": "xxx2bb46be6-f071-413d-9221-c090a8f0cb29",
	      "project_build_tool": "gradle",
	      "project_desc": ""
    }
]
```
#### Query Parameters
- *project_build_tool*: filter by ``project_build_tool``
- *project_id*: filter by  ``project_id``

### POST /projects/
#### Body
```json
[
	{
	      "project_id": "2bb46be6-f071-413d-9221-c090a8f0cb29",
	      "project_build_tool": "gradle",
	      "project_desc": ""
    }
]
```
### GET /projects/<project_id>/
#### Response (CODE HTTP200)
```json
[
	{
	      "project_id": "2bb46be6-f071-413d-9221-c090a8f0cb29",
	      "project_build_tool": "gradle",
	      "project_desc": "",
	      "project_apps": [     
					        {
					            "app_id": "dummy_app",
					            "app_location": "/Users/dummyUser/apps/dummyApp",
					            "app_description": "dumb",
					            "app_version": 1.1,
					            "app_flavor": "demo",
					            "app_build_type": "",
					            "app_project": "xxxx-dummy-xxxx-project-test"
					        }
    					  ]
    }
]
```

### GET /projects/<project_id>/
#### Response (CODE HTTP200)
```json
[
    {
        "project_id": "FutExam",
        "project_build_tool": "gradle",
        "project_desc": "",
        "project_apps": [
            {
                "app_id": "FutExam--714809332",
                "app_package": "com.ruirua.futexam",
                "app_description": "football quizz",
                "app_version": "0.0",
                "app_flavor": "full",
                "app_build_type": "debug",
                "app_project": "FutExam"
            }
        ]
    }

]
```


### GET /apps/
#### Query Parameters
- *app_id*: filter by  ``app_id``
- *app_description*: filter if contains``app_description``
- *app_permission*: filter apps that have the provided permission
- *app_flavor*: filter by   ``app_flavor``  (demo | full)
- *app_build_type*: filter by ``app_build_type`` (debug|release)
- *app_project*: filter by Android Project ID  ``app_project`` 

#### Response (CODE HTTP200)
```json
[
  {
    "app_id": "dummy_app",
    "app_location": "http://greensource.di.uminho.pt/dummy_app.zip",
    "app_description": "dumb",
    "app_version": 1.1,
    "app_flavor": "demo",
    "app_build_type": "",
    "app_project": "xxxx-dummy-xxxx-project-test"
    },
    ...
]
```

### POST /apps/
#### Body
```json
[
  {
    "app_id": "dummy_app",
    "app_location": "http://greensource.di.uminho.pt/dummy_app.zip",
    "app_description": "dumb",
    "app_version": 1.1,
    "app_flavor": "demo",
    "app_build_type": "",
    "app_project": "xxxx-dummy-xxxx-project-test"
    
  }
]
```

#### Response (CODE HTTP200)
```json
[
  {
    "app_id": "dummy_app",
    "app_location": "http://greensource.di.uminho.pt/dummy_app.zip",
    "app_description": "dumb",
    "app_version": 1.1,
    "app_flavor": "demo",
    "app_build_type": "",
    "app_project": "xxxx-dummy-xxxx-project-test"
    }

]
```

### GET /apps/permissions/
#### Query Parameters
- *application*: filter by  ``application``
- *permission*: filter by   ``android.permission`` ( internet | write_external_storage | ...)

#### Response (CODE HTTP200)
```json
[
    {
        "application": "dummy_app",
        "permission": "read_external_storage"
    },
    {   
        "application": "dummy_app",
        "permission": "read_profile"
    }
]
```


### GET /apps/metrics/
#### Query Parameters
- *app_name*: filter by  ``app_name`` 
- *app_metric*: filter by  ``app_metric`` 
- *app_metric_value*: filter by   ``app_metric_value``

#### Response (CODE HTTP200)
```json
[
   {
        "app_id": "dummy_app",
        "app_location": "http://greensource.di.uminho.pt/dummy_app.zip",
        "app_description": "dumb",
        "app_version": 1.1,
        "app_flavor": "demo",
        "app_build_type": "",
        "app_project": "xxxx-dummy-xxxx-project-test",
        "app_metrics": [
            {
                "am_app": "dummy_app",
                "am_metric": "nr_classes",
                "am_value": 1,
                "am_coeficient": 1,
                "am_test_result" : 1
        ]
    }
]
```

### POST /apps/metrics
#### Body
```json
[
    {
        "am_app": "dummy_app",
        "am_metric": "nr_classes",
        "am_value_text": "",
        "am_coeficient": 1,
        "am_test_result" : 1
    }
]
```

#### Response (CODE HTTP200)
```json
[
  { {
        "app_id": "dummy_app",
        "app_location": "http://greensource.di.uminho.pt/dummy_app.zip",
        "app_description": "dumb",
        "app_version": 1.1,
        "app_flavor": "demo",
        "app_build_type": "",
        "app_project": "xxxx-dummy-xxxx-project-test",
        "app_metrics": [
            {
                "am_app": "dummy_app",
                "am_metric": "nr_classes",
                "am_value_text": "",
                "am_coeficient": 1,
                "am_test_result" : 1
            }
        ]
    }

]
```

### GET /apps/<app_id>/
#### Response
```json
[
  {
    "app_id": "dummy_app",
    "app_description": "dummy",
    "app_version": 1.1,
    "app_flavor": "demo",
    "app_build_type": "",
    "app_project": "xxxx-dummy-xxxx-project-test"
    }
]
```

## GET /apps/<app_id>/classes/
- *class_package*: filter by  ``class_package``
- *class_name*: filter by   ``class_name``
- *class_non_acc_mod*: filter by  ``class_non_acc_mod``
- *class_language*: filter by   ``class_language``

#### Response (CODE HTTP200)
```json
[
    {
        "class_id": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
        "class_name": "com.ruirua.futexam.database.AppDatabase",
        "class_package": "com.ruirua.futexam.database",
        "class_app": "FutExam--714809332",
        "class_language": "java"
    }
]
```

### POST /apps/<app_id>/classes/
#### Body
```json
[
    {
        "class_id": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
        "class_name": "com.ruirua.futexam.database.AppDatabase",
        "class_package": "com.ruirua.futexam.database",
        "class_app": "FutExam--714809332",
        "class_language": "java"
    }
]
```

#### Expected Response (CODE HTTP200)
```json
[
    {
        "class_id": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
        "class_name": "com.ruirua.futexam.database.AppDatabase",
        "class_package": "com.ruirua.futexam.database",
        "class_app": "FutExam--714809332",
        "class_language": "java"
    }
]
```

## GET /apps/<app_id>/methods/
- *method_id*: filter by  ``method_id`` 
- *method_name*: filter by   ``method_name``
- *method_return*: filter by   ``method_return``
- *method_class*: filter by   ``method_class``
- *method_modifier*: filter modifier contained in  ``method_modifiers``


#### Response (CODE HTTP200)
```json
[
    {
        "method_id": "1640155663--getInstance--951530927",
        "method_name": "getInstance",
        "method_args": "android.content.Context",
        "method_return": "com.ruirua.futexam.database.AppDatabase",
        "method_class": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
        "method_modifiers": "public static"
    }
]
```


## GET /apps/<app_id>/methods/<method_id>/

#### Response (CODE HTTP200)
```json
[
    {
        "method_id": "1640155663--getInstance--951530927",
        "method_name": "getInstance",
        "method_args": "android.content.Context",
        "method_return": "com.ruirua.futexam.database.AppDatabase",
        "method_modifiers": "public static",
        "method_class": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
        "method_metrics": [
            {
                "mm_method": "1640155663--getInstance--951530927",
                "mm_metric": "api",
                "mm_value_text": "android.arch.persistence.room.Room.databaseBuilder(android.content.Context,java.lang.Class,java.lang.String)|android.arch.persistence.room.RoomDatabase",
                "mm_coeficient": "1",
                "mm_test_result": 32
            }
        ]
    }
]
```


## GET /apps/<app_id>/tests/

### retrieves the diferent combinations of testing already performed over application <app_id>

- *test_tool*: filter by  ``test_tool`` 
- *test_orientation*: filter by   ``test_orientation``

#### Response (CODE HTTP200)
```json
[
    {
        "id": 35,
        "test_application": "FutExam--714809332",
        "test_tool": "monkey",
        "test_orientation": "testoriented"
    },
    {
        "id": 34,
        "test_application": "FutExam--714809332",
        "test_tool": "monkeyrunner",
        "test_orientation": "testoriented"
    }
]
```

## GET /apps/<app_id>/tests/results/
### retrieves all tests performed for app <app_id> and respective test metrics

- *test_results_description*: filter by string contained in ``test_results_description`` 
- *test_results_device_state*: filter by  ``test_results_device_state`` 
- *test_results_seed*: filter by  ``test_seed`` 
- *test_results_profiler*: filter by   ``test_results_profiler``

#### Response (CODE HTTP200)
```json
[
    {
        "test_results_id": 30,
        "test_results_unix_timestamp": 1571417443,
        "test_results_seed": "0",
        "test_results_description": "",
        "test_results_test": 34,
        "test_results_profiler": "trepn",
        "test_results_device_state": 74,
        "test_metrics": [
            {
                "test_results": 30,
                "metric": "batterypower",
                "value_text": "0.00,0.00,0.00",
                "coeficient": "uW"
            },
        ]
    }
]
```

## GET /classes/
### retrieves all classes contained in the DB
- *class_package*: filter by  ``class_package``
- *class_name*: filter by   ``class_name``
- *class_non_acc_mod*: filter by  ``class_non_acc_mod``
- *class_language*: filter by   ``class_language``

#### Response (CODE HTTP200)
```json
[
   {
        "class_id": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
        "class_name": "com.ruirua.futexam.database.AppDatabase",
        "class_package": "com.ruirua.futexam.database",
        "class_app": "FutExam--714809332",
        "class_language": "java"
    }
]
```

### POST /classes/
#### Body
```json
[
   {
        "class_id": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
        "class_name": "com.ruirua.futexam.database.AppDatabase",
        "class_package": "com.ruirua.futexam.database",
        "class_app": "FutExam--714809332",
        "class_language": "java"
    }
]
```

#### Expected Response (CODE HTTP200)
```json
[
    {
        "class_id": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
        "class_name": "com.ruirua.futexam.database.AppDatabase",
        "class_package": "com.ruirua.futexam.database",
        "class_app": "FutExam--714809332",
        "class_language": "java"
    }
]
```



## GET /classes/metrics/
### retrieves all classes and respective class metrics

- *class_name*: filter classes by  ``class_name`` 
- *class_metric*: filters classes by metric ``class_metric`` 


#### Response (CODE HTTP200)
```json
[
    { 
        "class_id": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
        "class_name": "com.ruirua.futexam.database.AppDatabase",
        "class_package": "com.ruirua.futexam.database",
        "class_app": "FutExam--714809332",
        "class_language": "java",
        "class_imports": [],
        "class_metrics": [
            {
                "cm_class": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
                "cm_test_result": 32,
                "cm_metric": "nr_methods",
                "cm_coeficient": "1",
                "cm_value_text": "5"
            }
        ]
     }     
]
```

### POST /classes/metrics/
#### Body
```json
[
    { 
        "class_id": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
        "class_name": "com.ruirua.futexam.database.AppDatabase",
        "class_package": "com.ruirua.futexam.database",
        "class_app": "FutExam--714809332",
        "class_language": "java",
        "class_imports": [],
        "class_metrics": [
            {
                "cm_class": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
                "cm_test_result": 32,
                "cm_metric": "nr_methods",
                "cm_coeficient": "1",
                "cm_value_text": "5"
            }
        ]
     }  
]
```

#### Expected Response (CODE HTTP200)
```json
[
    { 
        "class_id": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
        "class_name": "com.ruirua.futexam.database.AppDatabase",
        "class_package": "com.ruirua.futexam.database",
        "class_app": "FutExam--714809332",
        "class_language": "java",
        "class_imports": [],
        "class_metrics": [
            {
                "cm_class": "FutExam--714809332--com--ruirua--futexam--database--AppDatabase",
                "cm_test_result": 32,
                "cm_metric": "nr_methods",
                "cm_coeficient": "1",
                "cm_value_text": "5"
            }
        ]
     }  
]
```




## GET /devices/
### retrieves all devices that were under test 
- *device_serial_number*: filter by  ``device_serial_number`` 
- *device_brand*: filter by  ``device_brand`` 
- *device_model*: filter by   ``device_model``


#### Response (CODE HTTP200)
```json
[
    {
        "device_serial_number": "79b3f648",
        "device_brand": "xiaomi",
        "device_model": "mi5",
        "device_cores": 4,
        "device_ram": "2775028kB",
        "device_max_cpu_freq": "2.15"
    }
]
```

### POST /devices/
#### Body
```json
[
    {
        "device_serial_number": "79b3f648",
        "device_brand": "xiaomi",
        "device_model": "mi5",
        "device_cores": 4,
        "device_ram": "2775028kB",
        "device_max_cpu_freq": "2.15"
    }
]
```

#### Expected Response (CODE HTTP200)
```json
[
    {
        "device_serial_number": "79b3f648",
        "device_brand": "xiaomi",
        "device_model": "mi5",
        "device_cores": 4,
        "device_ram": "2775028kB",
        "device_max_cpu_freq": "2.15"
    }
]
```

## GET /devicestate/
### retrieves all of the different states of the devices  when under testing

- *state_id*: filter by ID of state ``state_id`` 
- *state_api_version*: filter by Android API version  ``state_api_version`` 
- *state_os_version*: filter by OS version   ``state_os_version``
- *state_device_id*: filter by device   ``state_device_id``


#### Response (CODE HTTP200)
```json
[
    {
        "state_id": 74,
        "state_os_version": "8.0.0",
        "state_date": "2019-10-18T17:13:56.724329Z",
        "state_miui_version": "V10",
        "state_kernel_version": "Linux version 3.18.71-perf-gcbf6f59 (builder@c3-miui-ota-bd76.bj) (gcc version 4.9.x 20150123 (prerelease) (GCC) ) #1 SMP PREEMPT Fri Aug 31 17:46:24 CST 2018",
        "state_api_version": 26.0,
        "state_device_id": "79b3f648",
        "state_operator": "WTF",
        "state_operator_country": "pt"
    }
]
```

### POST /devicestate/
#### Body
```json
[
    {
        "state_id": 74,
        "state_os_version": "8.0.0",
        "state_date": "2019-10-18T17:13:56.724329Z",
        "state_miui_version": "V10",
        "state_kernel_version": "Linux version 3.18.71-perf-gcbf6f59 (builder@c3-miui-ota-bd76.bj) (gcc version 4.9.x 20150123 (prerelease) (GCC) ) #1 SMP PREEMPT Fri Aug 31 17:46:24 CST 2018",
        "state_api_version": 26.0,
        "state_device_id": "79b3f648",
        "state_operator": "WTF",
        "state_operator_country": "pt"
    }
]
```

#### Expected Response (CODE HTTP200)
```json
[
    {
        "state_id": 74,
        "state_os_version": "8.0.0",
        "state_date": "2019-10-18T17:13:56.724329Z",
        "state_miui_version": "V10",
        "state_kernel_version": "Linux version 3.18.71-perf-gcbf6f59 (builder@c3-miui-ota-bd76.bj) (gcc version 4.9.x 20150123 (prerelease) (GCC) ) #1 SMP PREEMPT Fri Aug 31 17:46:24 CST 2018",
        "state_api_version": 26.0,
        "state_device_id": "79b3f648",
        "state_operator": "WTF",
        "state_operator_country": "pt"
    }
]
```

## GET /tests/
### retrieves all testing combinations already executed
- *test_tool*: filter by  ``test_tool`` 
- *test_orientation*: filter by   ``test_orientation``
- *test_application*: filter by   ``test_application``


#### Response (CODE HTTP200)
```json
[
    {
        "id": 1,
        "test_application": "dummy_app",
        "test_tool": "monkey",
        "test_orientation": "testoriented"
    }
]
```

### POST /tests/
#### Body
```json
[
    {
        "id": 1,
        "test_application": "dummy_app",
        "test_tool": "junit",
        "test_orientation": "testoriented"
    }
]
```

#### Expected Response (CODE HTTP200)
```json
[
    {
        "id": 1,
        "test_application": "dummy_app",
        "test_tool": "junit",
        "test_orientation": "testoriented"
    }
]
```

## GET /tests/<test_id>/results/
### retrives every test execution and respective test-related metrics
- *test_results_id*: filter by  ``test_results_id`` 
- *test_results_seed*: filter by  ``test_results_seed`` 
- *test_results_description*: contains description in    ``test_results_description``
- *test_results_profiler*: filter by  ``test_results_profiler``
- *test_results_device_state*: filter by  ``test_results_device`` 

#### Response (CODE HTTP200)
```json
[
    {
        "test_results_id": 30,
        "test_results_unix_timestamp": 1571417443,
        "test_results_seed": "0",
        "test_results_description": "",
        "test_results_test": 34,
        "test_results_profiler": "trepn",
        "test_results_device_state": 74,
        "test_metrics": [
            {
                "test_results": 30,
                "metric": "batterypower",
                "value_text": "0.00,0.00,0.00",
                "coeficient": "uW"
            }
        ]
    }
]
```

### POST /tests/<test_id>/results/
#### Body
```json
[ 
	{
	    "test_results_id": 1,
	    "test_results_timestamp": "2018-09-11T13:46:59.115448Z",
	    "test_results_seed": 1893,
	    "test_results_description": "dd",
	    "test_results_test": 1,
	    "test_results_profiler": "trepn",
	    "test_results_device": "X2222"
   	}
]
```

#### Expected Response (CODE HTTP200)
```json
[
    {
	    "test_results_id": 1,
	    "test_results_timestamp": "2018-09-11T13:46:59.115448Z",
	    "test_results_seed": 1893,
	    "test_results_description": "dd",
	    "test_results_test": 1,
	    "test_results_profiler": "trepn",
	    "test_results_device": "X2222"
   	}
]
```

## GET /tests/metrics/
### retrieves all test-related metrics obtained 

- *test_metric*: filter by  ``test_metric`` 
- *test_value*: filter by  ``test_value`` 
- *test_results*: filter by  ``test_results`` 

#### Response (CODE HTTP200)
```json
[
   {
        "test_results": 30,
        "metric": "end_used_cpu",
        "value_text": "4.56/4.67/4.92",
        "coeficient": "%"
    }
]
```

### POST /tests/metrics/
#### Body
```json
[ 
	{
        "test_results": 30,
        "metric": "end_used_cpu",
        "value_text": "4.56/4.67/4.92",
        "coeficient": "%"
    }
]
```

#### Expected Response (CODE HTTP200)
```json
[
    {
        "test_results": 30,
        "metric": "end_used_cpu",
        "value_text": "4.56/4.67/4.92",
        "coeficient": "%"
    }
]
```

### POST tests/results/
#### Body
```json
[ 
	{
        "test_results_id": 1,
        "test_results_timestamp": "2018-09-11T13:46:59.115448Z",
        "test_results_seed": 1893,
        "test_results_description": "dd",
        "test_results_test": 1,
        "test_results_profiler": "trepn",
        "test_results_device": "X2222",
        "test_results_device_begin_state": 1,
        "test_results_device_end_state": 2
    }
]
```

#### Expected Response (CODE HTTP200)
```json
[
    {
        "test_results_id": 4,
        "test_results_timestamp": "2018-09-11T13:46:59.115448Z",
        "test_results_seed": 1893,
        "test_results_description": "dd",
        "test_results_test": 1,
        "test_results_profiler": "trepn",
        "test_results_device": "X2222",
        "test_results_device_begin_state": 1,
        "test_results_device_end_state": 2
    }
]
```

## GET /results/
- *test_results_id*: filter by  ``test_results_id`` 
- *test_results_seed*: filter by  ``test_results_seed`` 
- *test_results_description*: contains description in    ``test_results_description``
- *test_results_profiler*: filter by  ``test_results_profiler`` 
- *test_results_device*: filter by  ``test_results_device`` 

#### Response (CODE HTTP200)
```json
[
    {
        "test_results_id": 1,
        "test_results_timestamp": "2018-09-11T13:46:59.115448Z",
        "test_results_seed": 1893,
        "test_results_description": "dd",
        "test_results_test": 1,
        "test_results_profiler": "trepn",
        "test_results_device": "X2222",
        "test_results_device_begin_state": 1,
        "test_results_device_end_state": 2
    },
    {
        "test_results_id": 2,
        "test_results_timestamp": "2018-10-11T13:46:59.115448Z",
        "test_results_seed": 18931,
        "test_results_description": "dd",
        "test_results_test": 2,
        "test_results_profiler": "trepn",
        "test_results_device": "X2222",
        "test_results_device_begin_state": 3,
        "test_results_device_end_state": 4
    }
]
```

### POST /results/
#### Body
```json
[ 
	 {
        "test_results_id": 2,
        "test_results_timestamp": "2018-10-11T13:46:59.115448Z",
        "test_results_seed": 18931,
        "test_results_description": "dd",
        "test_results_test": 2,
        "test_results_profiler": "trepn",
        "test_results_device": "X2222",
        "test_results_device_begin_state": 3,
        "test_results_device_end_state": 4
    }
]
```

#### Expected Response (CODE HTTP200)
```json
[
     {
        "test_results_id": 2,
        "test_results_timestamp": "2018-10-11T13:46:59.115448Z",
        "test_results_seed": 18931,
        "test_results_description": "dd",
        "test_results_test": 2,
        "test_results_profiler": "trepn",
        "test_results_device": "X2222",
        "test_results_device_begin_state": 3,
        "test_results_device_end_state": 4
    }
]
```

## GET /methods/
- *method_name*: filter by  ``method_name`` 
- *method_class*: filter by  ``method_class`` 
- *method_metric*: filter by  ``mm_metric`` 
- *method_metric_value*: filter by  ``mm_value`` 
- *method_metric_value_gte*: filter by  ``mm_value > value`` 
- *method_metric_value_lte*: filter by  ``mm_value < value`` 




#### Response (CODE HTTP200)
```json
[
    {
        "method_id": "com.dummy.dummyapp.DummyActivity.dummyMethod",
        "method_name": "dummyMethod",
        "method_acc_modifier": "public",
        "method_non_acc_mod": "static",
        "method_class": "com.dummy.dummyapp.DummyActivity",
        "method_metrics": [
            {
                "mm_method": "com.dummy.dummyapp.DummyActivity.dummyMethod",
                "mm_metric": "totalenergy",
                "mm_value": 13,
                "mm_coeficient": 1,
                "mm_method_invoked": null
            }
        ]
    },
    {
        "method_id": "com.dummy.dummyapp.DummyActivity.dummyMethod2",
        "method_name": "dummyMethod2",
        "method_acc_modifier": "private",
        "method_non_acc_mod": "",
        "method_class": "com.dummy.dummyapp.DummyActivity",
        "method_metrics": []
    }
]
```

### POST /methods/
#### Body
```json
[
     {
        "method_id": "com.dummy.dummyapp.DummyActivity.dummyMethod",
        "method_name": "dummyMethod",
        "method_acc_modifier": "public",
        "method_non_acc_mod": "static",
        "method_class": "com.dummy.dummyapp.DummyActivity"
    }
]
```

#### Expected Response (CODE HTTP200)
```json
[
     {
        "method_id": "com.dummy.dummyapp.DummyActivity.dummyMethod",
        "method_name": "dummyMethod",
        "method_acc_modifier": "public",
        "method_non_acc_mod": "static",
        "method_class": "com.dummy.dummyapp.DummyActivity"
    }
]
```

## GET /methods/
- *method_name*: filter by  ``method_name`` 
- *method_class*: filter by  ``method_class`` 
- *method_metric*: filter by  ``mm_metric`` 
- *method_metric_value*: filter by  ``mm_value`` 
- *method_metric_value_gte*: filter by  ``mm_value > value`` 
- *method_metric_value_lte*: filter by  ``mm_value < value`` 


#### Response (CODE HTTP200)
```json
[
    {
        "method_id": "com.dummy.dummyapp.DummyActivity.dummyMethod",
        "method_name": "dummyMethod",
        "method_acc_modifier": "public",
        "method_non_acc_mod": "static",
        "method_class": "com.dummy.dummyapp.DummyActivity",
        "method_metrics": [
            {
                "mm_method": "com.dummy.dummyapp.DummyActivity.dummyMethod",
                "mm_metric": "totalenergy",
                "mm_value": 13,
                "mm_coeficient": 1,
                "mm_method_invoked": null
            }
        ]
    },
    {
        "method_id": "com.dummy.dummyapp.DummyActivity.dummyMethod2",
        "method_name": "dummyMethod2",
        "method_acc_modifier": "private",
        "method_non_acc_mod": "",
        "method_class": "com.dummy.dummyapp.DummyActivity",
        "method_metrics": []
    }
]
```

### POST /methods/
#### Body
```json
[
     {
        "method_id": "com.dummy.dummyapp.DummyActivity.dummyMethod",
        "method_name": "dummyMethod",
        "method_acc_modifier": "public",
        "method_non_acc_mod": "static",
        "method_class": "com.dummy.dummyapp.DummyActivity"
    }
]
```

#### Expected Response (CODE HTTP200)
```json
[
     {
        "method_id": "com.dummy.dummyapp.DummyActivity.dummyMethod",
        "method_name": "dummyMethod",
        "method_acc_modifier": "public",
        "method_non_acc_mod": "static",
        "method_class": "com.dummy.dummyapp.DummyActivity"
    }
]
```

## GET /methods/metrics/
- *method_name*: filter by  ``method_name`` 
- *method_class*: filter by  ``method_class`` 
- *method_app*: filter by  ``app_id`` 


#### Response (CODE HTTP200)
```json
[
    {
        "method_id": "com.dummy.dummyapp.DummyActivity.dummyMethod",
        "method_name": "dummyMethod",
        "method_acc_modifier": "public",
        "method_non_acc_mod": "static",
        "method_class": "com.dummy.dummyapp.DummyActivity",
        "method_metrics": [
            {
                "mm_method": "com.dummy.dummyapp.DummyActivity.dummyMethod",
                "mm_metric": "totalenergy",
                "mm_value": 13,
                "mm_coeficient": 1,
                "mm_method_invoked": null
            }
        ]
    },
    {
        "method_id": "com.dummy.dummyapp.DummyActivity.dummyMethod2",
        "method_name": "dummyMethod2",
        "method_acc_modifier": "private",
        "method_non_acc_mod": "",
        "method_class": "com.dummy.dummyapp.DummyActivity",
        "method_metrics": []
    }
]
```

### POST /methods/metrics/
#### inserts methods and metrics in repo
#### Body
```json
[
     {
        "method_id": "com.dummy.dummyapp.DummyActivity.dummyMethod2",
        "method_name": "dummyMethod2",
        "method_acc_modifier": "private",
        "method_non_acc_mod": "",
        "method_class": "com.dummy.dummyapp.DummyActivity",
        "method_metrics": []
    }
]
```

#### Expected Response (CODE HTTP200)
```json
[
     {
        "method_id": "com.dummy.dummyapp.DummyActivity.dummyMethod2",
        "method_name": "dummyMethod2",
        "method_acc_modifier": "private",
        "method_non_acc_mod": "",
        "method_class": "com.dummy.dummyapp.DummyActivity",
        "method_metrics": []
    }
]
```


### POST /methods/invoked/
#### inserts invokation of method by test in repo
#### Body
```json
[
     {
        "method": "com.dummy.dummyapp.DummyActivity.dummyMethod",
        "test_results": "1"
    }
]
```

#### Expected Response (CODE HTTP200)
```json
[
	{
        "method": "com.dummy.dummyapp.DummyActivity.dummyMethod",
        "test_results": "1"
    }
]
```


