# **NOTIFIER SERVICE**

_To check the code_

`python index.py`

_To change the change notifying configuration, see the **notify_config.json** file._

_Config example_

    "Company": {
            "fields": [
                "is_deleted",
                {"crawling_status": {"from": 13, "to": 10}}
            ],
            "when_created": true,
            "when_physically_deleted": true,
            "notify": "Company"
    }


1) **`fields` property value can be set in 2 ways**
   1) For simple changes, just add the name of the property we want to track for changes
   2) To track the change **FROM** **TO** value, we need to add a dictionary element, the key will be the name of the property, and the dictionary keys will be `from` and `to`<br> Ex.<br> `{"is_deleted": {"from": false, "to": true}}`
2) `when_created` if set and the value is `true`, the service will notify about the creation of the object
3) `when_physically_deleted` if set and the value is `true`, the service will notify that the object has been physically deleted
4) `notify`, if set and the value is different from the name of the configuration object, the service will notify that changes have been made from notify value object. <br>   Ex. _Company's CompanyCompetitor changed_ <br> Where `Company` is the value of `notify` <br> Note. `notify` default value is self