# -*- coding: utf-8 -*-
import pymysql

dbuser = 'root'
dbpass = '123456'
dbname = 'retweet'
dbhost = 'localhost'
dbport = '3306'

class MicroblogPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT ignore INTO demo_weiboinfo(mblog_id,mblog_created_at,mblog_reposts_count,mblog_comments_count,mblog_attitudes_count,mblog_raw_text,mblog_pid,mblog_oid,mblog_layer,usr_id)
                                        VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)""",
                                (
                                    item['mblog_id'].encode('utf-8'),
                                    item['mblog_created_at'].encode('utf-8'),
                                    item['mblog_reposts_count'],
                                    item['mblog_comments_count'],
                                    item['mblog_attitudes_count'],
                                    item['mblog_raw_text'].encode('utf-8'),
                                    item['mblog_pid'].encode('utf-8'),
                                    item['mblog_oid'].encode('utf-8'),
                                    item['mblog_layer'],
                                    item['usr_id'].encode('utf-8'),
                                )
                                )
            self.conn.commit()
        except pymysql.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

        return item



