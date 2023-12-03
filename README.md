*** QUY TRINH THUC HIEN PROJECT ***

1. Collect/Crawl data with scrapy from multiple sources (Topcv, VietnameWork,...)




*** CAY PHAN CAP PROJECT ***
data_engineer_intern_project/
│
├── dags/
│   ├── crawl_data_dag.py              
│   ├── process_data_dag.py
│   └── etl_dag.py
│
├── scripts/
│   ├── crawl_data/
│   │   ├── website1_crawler.py
│   │   └── website2_crawler.py
│   ├── process_data.py
│   ├── stored_procedures/
│   │   └── date_processing.sql
│   └── dimensional_modeling/
│       └── create_dimension_tables.sql
│
├── config/
│   ├── config.py
│   └── credentials.json
│
├── data/
│   ├── raw_data/
│   │   ├── website1/
│   │   └── website2/
│   └── processed_data/
│
├── database/
│   ├── schema.sql
│   └── migrations/
│
├── dimensional_model/
│   └── dim_date.sql
│
├── etl/
│   ├── extract_data.py
│   ├── transform_data.py
│   └── load_data.py
│
├── analytics/
│   ├── generate_reports.py
│   └── perform_analysis.py
│
├── monitoring/
│   ├── log/
│   │   ├── crawler_logs.log
│   │   ├── etl_logs.log
│   │   ├── analytics_logs.log
│   │   └── error_logs.log
│   ├── test/
│   │   ├── test_crawler.py
│   │   ├── test_etl.py
│   │   └── test_analytics.py
│   └── documentation/
│       ├── data_dictionary.md
│       └── etl_process.md
│
├── version_control/
│   ├── git/
│   └── .gitignore
│
└── docker/
    ├── Dockerfile
    └── requirements.txt



