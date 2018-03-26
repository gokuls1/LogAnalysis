#!/usr/bin/env python

import psycopg2


def connect(db_name="news"):
    """Connect to the PostgreSQL database"""
    try:
        db = psycopg2.connect("dbname={}".format(db_name))
        cursor = db.cursor()
        return db, cursor
        Print("Database Connect")
    except:
        print("Unable to connect to the database")


def article():
    """Most popular three articles of all time"""
    db, cursor = connect()
    query = (
        "select articles.title, count(*) as views "
        "from articles inner join log on log.path "
        "like concat('%', articles.slug, '%') "
        "where log.status like '%200%' group by "
        "articles.title, log.path order by views desc limit 3")
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    print "\nWhat Are The Most Popular Three Articles Of All Time?\n"
    for i in range(0, len(result), 1):
        print str(i + 1) + ". \"" + result[i][0] + "\" Is "\
            + str(result[i][1]) + " Views"


def authors():
    """Popular article authors of all time"""
    db, cursor = connect()
    query = (
        "select authors.name, count(*) as views from articles inner "
        "join authors on articles.author = authors.id inner join log "
        "on log.path like concat('%', articles.slug, '%') where "
        "log.status like '%200%' group "
        "by authors.name order by views desc")
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    print "\nWho Are The Most Popular Article Authors Of All Time?\n"
    for i in range(0, len(result), 1):
        print str(i + 1) + ". \"" + result[i][0] + "\" Is "\
            + str(result[i][1]) + " Views"


def status():
    """Days on which more than 1% of requests lead to errors"""
    db, cursor = connect()
    query = (
        "select day, perc from ("
        "select day, round((sum(requests)/(select count(*) from log where "
        "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
        "perc from (select substring(cast(log.time as text), 0, 11) as day, "
        "count(*) as requests from log where status like '%404%' group by day)"
        "as log_percentage group by day order by perc desc) as final_query "
        "where perc >= 1")
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    print "\nOn which days did more than 1% of requests lead to errors?\n"
    for i in range(0, len(result), 1):
        print "On " + str(result[i][0]) + " Error Found Is "\
            + str(result[i][1]) + "%\n"


if __name__ == '__main__':

    article()
    authors()
    status()
