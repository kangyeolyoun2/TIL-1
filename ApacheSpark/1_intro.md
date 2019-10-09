
# Chaper 1. 아파치 스파크란?
- `통합 컴퓨팅 엔진`으로 클러스터 환경에서 `데이터를 병렬로 처리`하는 라이브러리 집합.
- 여러 개발자와 데이터 과학자에게 표준도구가 되어가고 있음.
- 널리 쓰이는 4가지 언어(자바, 스칼라, 파이썬 , R)를 지원하며, SQL뿐만 아니라 스트리밍, 머신러닝에 이르기까지 넓은 범위의 라이브러리를 제공. 
- 단일 노트북 환경에서부터 수천 대의 서버로 구성된 `클러스터`까지 다양한 환경에서 실행 가능. 

## 1.1 아파치 스파크의 철학

### 1) 통합 (unified)
- 간단한 데이터 읽기에서부터 SQL처리, 머신러닝, 스트림 처리에 이르기까지 다양한 데이터 분석 작업을 `같은 연산 엔진과 일관성 있는 API`로 수행할 수 있도록 설계. 
- 스파크 API는 사용자 애플리케이션에서 다른 라이브러리의 기능을 조합해 더 나은 성능을 발휘할 수 있도록 설계. 
- 스파크는 여러 통합 플랫폼과 유사한 사용 방식을 제공. 

### 2) 컴퓨팅 엔진
- 기능을 `컴퓨팅 엔진(연산 기능)`에 제한을 두며, 영구 저장소의 역할은 수행하지 않음.
- 애저 스토리지, 아마존 S3, 아파치 하둡, 아파치 카산드라, 아파치 카프카 등의 `저장소를 지원`.
- 서로 다른 저장소 시스템을 매우 유사하게 볼 수 있도록 설계. 
- 하둡 저장소와 잘 호환되며, 공개형 클라우드 환경이나 하둡 아키텍처를 사용할 수 없는 환경에서 많이 사용

### 3) 라이브러리 
- 스파크 컴포넌트는 통합 API를 제공하는 `통합 엔진 기반의 자체 라이브러리`. 
- 스파크 표준 라이브러리와 다양한 외부 라이브러리를 지원.

## 1.2 스파크의 등장 배경
- 프로세서의 성능 향상의 제약으로 단일 프로세서 성능을 향상시키는 것이 아닌 `병렬 CPU 코어를 추가`하는 방향으로 선회.
- 애플리케이션의 성능 향상을 위해 병렬 처리가 필요해짐


```python
import findspark
findspark.init()

import os
exec(open(os.path.join(os.environ["SPARK_HOME"], 'python/pyspark/shell.py')).read())
```

    Welcome to
          ____              __
         / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  '_/
       /__ / .__/\_,_/_/ /_/\_\   version 2.4.4
          /_/
    
    Using Python version 3.7.3 (default, Mar 27 2019 16:54:48)
    SparkSession available as 'spark'.


# Chapter 2. 스파크 간단히 살펴보기
- DataFrame, SQL을 사용한 클러스터, 스파크 애플리케이션
- 구조적 API

## 2.1 스파크 기본 아키텍처
- `컴퓨터 클러스터`는 여러 컴퓨터의 자원을 모아 하나의 컴퓨터처럼 사용. (대규모 정보를 연산할 만한 성능을 가짐.)
- 스파크는 클러스터에서 작업을 조율할 수 있는 프레임워크 역할을 하며, `클러스터의 데이터 처리 작업을 관리하고 조율`.
- `클러스터 매니저`에서 스파크가 연산에 사용할 클러스터를 관리함.
- 사용자는 클러스터 매니저에 스파크 애플리케이션을 제출하며, 클러스터 매니저는 애플리케이션 실행에 필요한 자원을 할당함.

### 스파크 애플리케이션
<img src="./TIL/ApacheSpark/imgs/3-1.jpeg" width="60%">

- `드라이버(driver) 프로세스`와 다수의 `익스큐터(executor) 프로세스`로 구성
- 드라이버 프로세스 : 스파크 애플리케이션 정보의 유지 관리, 사용자 프로그램이나 입력에 대한 응답, 전반적인 익스큐터 프로세스의 작업과 관련된 분석, 배포, 스케줄링 역할. 
- 익스큐터 프로세스 : 드라이버 프로세스가 할당한 작업 수행, 드라이버 프로세스에 보고. 
- 하나의 클러스터에서 여러 개의 스파크 애플리케이션 실행 가능.
- 대화형 모드로 스파크를 시작하면, 스파크 애플리케이션을 관리하는 `SparkSession`이 자동으로 생성

## 2.2 스파크 API
- 스파크 언어 API를 이용하면 다양한 프로그래밍 언어로 스파크 코드를 실행할 수 있음. 
- 스파크는 두 가지 API를 제공함. 
    - 비구조적 API
    - 구조적 API

## 2.3 SparkSession
- `스파크 애플리케이션을 제어`하는 드라이버 프로세스.
- 사용자가 정의한 처리 명령을 클러스터에서 실행.
- 하나의 SparkSession은 하나의 스파크 애플리케이션에 대응.

## 2.4 DataFrame
- 가장 대표적인 구조적 API.
- 스프레드시트와 유사하나, 스파크의 DataFrame은 수천 대의 컴퓨터에 분산되어 있음. 

### 파티션
- 모든 익스큐터가 병렬로 작업을 수행할 수 있도록 `파티션`이라 불리는 청크 단위로 데이터를 분할.
- 파티션은 클러스터의 물리적 머신에 존재하는 로우의 집합.
- DataFrame을 사용하면 파티션을 수동 혹은 개별적으로 처리할 필요가 없음. 


```python
myRange = spark.range(1000).toDF("number")
# 1개의 컬럼과 1000개의 로우로 구성된 DataFrame, 0 ~ 999까지의 값이 할당
# 숫자 범위의 각 부분이 서로 다른 익스큐터에 할당
```

## 2.5 트랜스포메이션
- 스파크의 핵심 데이터 구조는 `불변성을 지님`. 따라서 `변경`을 하려면 원하는`트랜스포메이션`명령을 스파크에 알려줘야함.
- 트랜스포메이션만 지정하고 액션을 호출하지 않으면 스파크는 실제 트랜스포메이션을 수행하지 않음. 
- 트랜스포메이션의 논리적 실행계획은 DataFrame의 계보나 스파크의 쿼리 실행 계획을 확인 가능.
- 실행 계획은 트랜스포메이션의 지향성 비순환 그래프. 
- 유형
    - 좁은 트랜스포메이션
        - 각 입력 파티션이 하나의 출력 파티션에만 영향을 미침. 
    - 넓은 트랜스포메이션
        - 하나의 입력 파티션이 여러 출력 파티션에 영향을 미침.
        - 셔플....(?)
 
### 지연 연산
- 특정 연산 명령이 내려진 즉시 데이터를 수정하지 않고, 원시 데이터에 적용할 `트랜스포메이션의 실행계획을 생성`.
- 실행계획은 디버깅과 스파크의 실행 과정을 이해하는 데 도움을 주는 도구.
- `전체 데이터 흐름을 최적화`하는 엄청난 강점을 지님. 

## 2.6 액션
- 실제 연산을 수행하기 위한 명령.
- 액션을 지정하면 `스파크 잡`이 시작. 
- 스파크 잡은 필터(좁은 트랜스포메이션)를 수행한 후 파티션별로 레코드 수를 카운트(넓은 트랜스포메이션)함. 각 언어에 적합한 네이티브 객체에 결과를 모음  .... (?)

## 2.7 스파크 UI
- 클러스터에서 실행 중인 `스파크 잡의 진행 상황을 모니터링`할 때 사용
- 스파크 잡을 튜닝하고 디버깅할 때 매우 유용. 

## 2.8 종합예제
- 미국 교통통계국의 항공운항 데이터
- reference : https://github.com/FVbros/Spark-The-Definitive-Guide/tree/master/data/flight-data

### 트랜스포메이션 메서드
- read: 좁은 트랜스 포메이션으로 동작
- sort :  넓은 트랜스 포메이션으로 동작
- explain
- 트랜스포메이션의 최종 결과는 가장 위에, 데이터 소스는 가장 아래에 위치. 


```python
# 데이터 읽기
# 스키마 정보를 알아내는 스키마 추론 기능 사용

flightData2015 = spark\
    .read\
    .option("inferSchema", "true")\
    .option("header", "true")\
    .csv("/Users/baek/Documents/Notebook/github/datas/2015-summary.csv")
```


```python
flightData2015.sort("count").explain()
```

    == Physical Plan ==
    *(2) Sort [count#24 ASC NULLS FIRST], true, 0
    +- Exchange rangepartitioning(count#24 ASC NULLS FIRST, 200)
       +- *(1) FileScan csv [DEST_COUNTRY_NAME#22,ORIGIN_COUNTRY_NAME#23,count#24] Batched: false, Format: CSV, Location: InMemoryFileIndex[file:/Users/baek/Documents/Notebook/github/datas/2015-summary.csv], PartitionFilters: [], PushedFilters: [], ReadSchema: struct<DEST_COUNTRY_NAME:string,ORIGIN_COUNTRY_NAME:string,count:int>


### 액션 실행 설정
- 셔플 수행 시 기본적으로 200개의 셔플 파티션 생성.
- 예제에서는 출력 파티션의 수를 5로 설정.


```python
spark.conf.set("spark.sql.shuffle.partitions", "5") 
flightData2015.sort("count").take(2)
```




    [Row(DEST_COUNTRY_NAME='United States', ORIGIN_COUNTRY_NAME='Singapore', count=1),
     Row(DEST_COUNTRY_NAME='Moldova', ORIGIN_COUNTRY_NAME='United States', count=1)]



### SQL 사용 작업
- 스파크 SQL을 사용하면 모든 DataFrame을 테이블이나 뷰(임시 테이블)로 등록한 후 SQL쿼리를 사용할 수 있음. 
- 스파크에서는 SQL쿼리를 DataFrame코드(R,파이썬,스칼라,자바 코드)와 같은 실행계획으로 컴파일함.


```python
# DataFrame을 테이블이나 뷰로 만듦.
flightData2015.createOrReplaceTempView("flight_data_2015")
```


```python
# 데이터 조회

# (1) 스파크 SQL쿼리 
sqlWay = spark.sql("""
    SELECT DEST_COUNTRY_NAME, count(1)
    FROM flight_data_2015
    GROUP BY DEST_COUNTRY_NAME
""")

sqlWay.explain()
```

    == Physical Plan ==
    *(2) HashAggregate(keys=[DEST_COUNTRY_NAME#22], functions=[count(1)])
    +- Exchange hashpartitioning(DEST_COUNTRY_NAME#22, 5)
       +- *(1) HashAggregate(keys=[DEST_COUNTRY_NAME#22], functions=[partial_count(1)])
          +- *(1) FileScan csv [DEST_COUNTRY_NAME#22] Batched: false, Format: CSV, Location: InMemoryFileIndex[file:/Users/baek/Documents/Notebook/github/datas/2015-summary.csv], PartitionFilters: [], PushedFilters: [], ReadSchema: struct<DEST_COUNTRY_NAME:string>



```python
# (2) DataFrame에 쿼리 수행
dataframeWay = flightData2015\
    .groupBy("DEST_COUNTRY_NAME")\
    .count()

dataframeWay.explain()
```

    == Physical Plan ==
    *(2) HashAggregate(keys=[DEST_COUNTRY_NAME#22], functions=[count(1)])
    +- Exchange hashpartitioning(DEST_COUNTRY_NAME#22, 5)
       +- *(1) HashAggregate(keys=[DEST_COUNTRY_NAME#22], functions=[partial_count(1)])
          +- *(1) FileScan csv [DEST_COUNTRY_NAME#22] Batched: false, Format: CSV, Location: InMemoryFileIndex[file:/Users/baek/Documents/Notebook/github/datas/2015-summary.csv], PartitionFilters: [], PushedFilters: [], ReadSchema: struct<DEST_COUNTRY_NAME:string>



```python
# 데이터 처리 메서드 예제

# (1) 스파크 sql쿼리 
spark.sql("""SELECT max(count) FROM flight_Data_2015""").take(1)
```




    [Row(max(count)=370002)]




```python
# (2) 파이썬 코드 
from pyspark.sql.functions import max
flightData2015.select(max("count")).take(1)
```




    [Row(max(count)=370002)]




```python
# 데이터 처리 메서드 예제

# (1) 스파크 sql쿼리 
maxsql = spark.sql("""
    SELECT DEST_COUNTRY_NAME, sum(count) as destination_total
    FROM flight_data_2015
    GROUP BY DEST_COUNTRY_NAME
    ORDER BY sum(count) DESC
    LIMIT 5
""")

maxsql.show()
```

    +-----------------+-----------------+
    |DEST_COUNTRY_NAME|destination_total|
    +-----------------+-----------------+
    |    United States|           411352|
    |           Canada|             8399|
    |           Mexico|             7140|
    |   United Kingdom|             2025|
    |            Japan|             1548|
    +-----------------+-----------------+
    



```python
#(2) 파이썬 코드 
from pyspark.sql.functions import desc

flightData2015\
    .groupBy("DEST_COUNTRY_NAME")\
    .sum("count")\
    .withColumnRenamed("sum(count)", "destination_total")\
    .sort(desc("destination_total"))\
    .limit(5)\
    .show()
```

    +-----------------+-----------------+
    |DEST_COUNTRY_NAME|destination_total|
    +-----------------+-----------------+
    |    United States|           411352|
    |           Canada|             8399|
    |           Mexico|             7140|
    |   United Kingdom|             2025|
    |            Japan|             1548|
    +-----------------+-----------------+
    



```python
# 실행계획
flightData2015\
    .groupBy("DEST_COUNTRY_NAME")\
    .sum("count")\
    .withColumnRenamed("sum(count)", "destination_total")\
    .sort(desc("destination_total"))\
    .limit(5)\
    .explain()
```

    == Physical Plan ==
    TakeOrderedAndProject(limit=5, orderBy=[destination_total#106L DESC NULLS LAST], output=[DEST_COUNTRY_NAME#22,destination_total#106L])
    +- *(2) HashAggregate(keys=[DEST_COUNTRY_NAME#22], functions=[sum(cast(count#24 as bigint))])
       +- Exchange hashpartitioning(DEST_COUNTRY_NAME#22, 5)
          +- *(1) HashAggregate(keys=[DEST_COUNTRY_NAME#22], functions=[partial_sum(cast(count#24 as bigint))])
             +- *(1) FileScan csv [DEST_COUNTRY_NAME#22,count#24] Batched: false, Format: CSV, Location: InMemoryFileIndex[file:/Users/baek/Documents/Notebook/github/datas/2015-summary.csv], PartitionFilters: [], PushedFilters: [], ReadSchema: struct<DEST_COUNTRY_NAME:string,count:int>

