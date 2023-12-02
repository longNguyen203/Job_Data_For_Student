*** QUY TRINH THUC HIEN PROJECT ***

1. Collect/Crawl data with scrapy from multiple sources (Topcv, VietnameWork,...)



















*** CAY PHAN CAP PROJECT ***
data_engineer_intern_project/
│
├── dags/
│   ├── crawl_data_dag.py
│   └── process_data_dag.py
│
├── scripts/
│   ├── process_data.py      -> Chua logic xu ly data
│   └── schedule_crawler.py  -> 
│
├── config/
│   ├── config.py
│   └── credentials.json
│
├── data/
│   ├── raw_data/            -> data tho
│   │   ├── website1/        -> Crawl from web first
│   │   └── website2/        -> Crawl from web second
│   └── processed_data/      -> data da dc xu ly
│
├── database/
│   ├── schema.sql
│   └── migrations/
│
├── logs/
│   ├── crawler_logs.log
│   └── processing_logs.log
│
├── tests/
│   ├── test_crawler.py
│   ├── test_data_processing.py
│   └── test_integration.py
│
├── docker/
│   ├── Dockerfile
│   └── requirements.txt
│
├── airflow/
│   ├── airflow.cfg
│   └── dags/
│
├── kafka/
│   └── kafka_producer.py
│
├── spark/
│   ├── spark_job.py
│   └── spark_submit.sh
│
├── dbt/
│   ├── analysis/
│   ├── data/
│   ├── macros/
│   └── models/
│
├── scrapy/
│   ├── scrapy_project/
│   │   ├── scrapy.cfg
│   │   └── scrapy_project/
│   │       ├── spiders/
│   │       │   └── your_spider.py
│   │       └── items.py
│   └── requirements.txt
│
├── requirements.txt
└── README.md

