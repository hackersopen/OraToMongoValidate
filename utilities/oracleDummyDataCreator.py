import cx_Oracle


def next_string(column):
	column_string = ""
	column_number = column
	while (column_number > 0):
		current_latter_number = (column_number - 1)%26
		current_latter = chr(current_latter_number+65)
		column_string = current_latter + column_string
		column_number = int((column_number - (current_latter_number+1))/26)
	return column_string

db = cx_Oracle.connect('Username/Password@127.0.0.1:1521/xe')
cursor = db.cursor()
for i in range (501,10001,1):
	current_varchar = next_string(i)
	cursor.execute('INSERT INTO resourceFunctionSpecification (rfsid, href) VALUES ('+str(i)+','+'\''+current_varchar+'\''+')')
	cursor.execute('INSERT INTO resourceFunctionLocation (rflid, href) VALUES ('+str(i)+','+'\''+current_varchar+'\''+')')
	cursor.execute('INSERT INTO resourceFunction (rfid, automodification, description, href, name, priority, version, rflid) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+'\''+current_varchar+'\''+','+'\''+current_varchar+'\''+','+'\''+current_varchar+'\''+','+str(i)+','+'\''+current_varchar+'\''+','+str(i)+')')
	cursor.execute('INSERT INTO scale (sid, href, scaleStatus, type) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+'\''+current_varchar+'\''+','+'\''+current_varchar+'\''+')')
	cursor.execute('INSERT INTO scheduleRef (srid, href, rfid) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+str(i)+')')
	cursor.execute('INSERT INTO resourceFunctionScheduleRef (rfsrid, href, srid) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+str(i)+')')
	cursor.execute('INSERT INTO scaleScheduleRef_JT (sid, srid) VALUES ('+str(i)+','+str(i)+')')
	cursor.execute('INSERT INTO characteristics (cid, name, value) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+str(i)+')')
	cursor.execute('INSERT INTO features (fid, name) VALUES ('+str(i)+','+'\''+current_varchar+'\''+')')
	cursor.execute('INSERT INTO featureGroup (fgid, name) VALUES ('+str(i)+','+'\''+current_varchar+'\''+')')
	cursor.execute('INSERT INTO resourceFunctionFeature (rffid, name, fid) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+str(i)+')')
	cursor.execute('INSERT INTO featureGroupCharacteristic (fgcid, type,fgid) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+str(i)+')')
	cursor.execute('INSERT INTO characteristicsFeatures_JT (fid, cid) VALUES ('+str(i)+','+str(i)+')')
	cursor.execute('INSERT INTO featuresFeatureGroup_JT (fid, fgid) VALUES ('+str(i)+','+str(i)+')')
	cursor.execute('INSERT INTO migrateLocation (mlid, location) VALUES ('+str(i)+','+'\''+current_varchar+'\''+')')
	cursor.execute('INSERT INTO migrate (mid, mlid, adminstatemodification, completionmode, migratestatus, starttime) VALUES ('+str(i)+','+str(i)+','+'\''+current_varchar+'\''+','+'\''+current_varchar+'\''+','+'\''+current_varchar+'\''+',sysdate)')
	cursor.execute('INSERT INTO healPolicy (hpid, policyname) VALUES ('+str(i)+','+'\''+current_varchar+'\''+')')
	cursor.execute('INSERT INTO heal (hid, hpid, cause, healaction, healstatus, starttime) VALUES ('+str(i)+','+str(i)+','+'\''+current_varchar+'\''+','+'\''+current_varchar+'\''+','+'\''+current_varchar+'\''+',sysdate)')
	cursor.execute('INSERT INTO nameValuePair (nvpid, name, value) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+str(i)+')')
	cursor.execute('INSERT INTO nameValuePairHeal_JT (hid, nvpid) VALUES ('+str(i)+','+str(i)+')')
	cursor.execute('INSERT INTO nameValuePairMigrate_JT (mid, nvpid) VALUES ('+str(i)+','+str(i)+')')
	cursor.execute('INSERT INTO sapref (saprid, href) VALUES ('+str(i)+','+'\''+current_varchar+'\''+')')
	cursor.execute('INSERT INTO migrateSapref (msaprid, priority, href, mid, saprid) VALUES ('+str(i)+','+str(i)+','+'\''+current_varchar+'\''+','+str(i)+','+str(i)+')')
	cursor.execute('INSERT INTO resourceFunctionSapRef (rfsaprid, href, saprid) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+str(i)+')')
	cursor.execute('INSERT INTO request (reqid, body, method, reqto) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+'\''+current_varchar+'\''+','+'\''+current_varchar+'\''+')')
	cursor.execute('INSERT INTO response (resid, body, statuscode) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+str(i)+')')
	cursor.execute('INSERT INTO requestHeader (reqhid, name, value, reqid) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+str(i)+','+str(i)+')')
	cursor.execute('INSERT INTO monitor (monid, sourcehref, state) VALUES ('+str(i)+','+'\''+current_varchar+'\''+','+'\''+current_varchar+'\''+')')
	cursor.execute('INSERT INTO requestMonitor_JT (monid, reqid) VALUES ('+str(i)+','+str(i)+')')
	cursor.execute('INSERT INTO responseRequestHeader (resid, reqhid) VALUES ('+str(i)+','+str(i)+')')
	print("Added Row:",i)
db.commit()
db.close()

