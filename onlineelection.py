import random
from flask import Flask, render_template, request, redirect, session,jsonify
import datetime
import demjson

from Dbconnection import Db
app = Flask(__name__)
app.secret_key="abc"

@app.route('/',methods=['get','post'])
def login():
    if request.method=="POST":
        db=Db()
        username=request.form['textfield']
        password=request.form['textfield2']
        res=db.selectOne("select * from login where username='"+username+"' and password='"+password+"'")
        if res is not None:
            if res['u_type']=='admin':
                session['lg'] = 'lin'
                return '''<script>alert('successful');window.location="/adminhome"</script>'''
            elif  res['u_type']=='worker':
                session['lg'] = 'lin'
                session['lid']=res['login_id']

                return '''<script>alert('successful');window.location="/workerhome"</script>'''
            elif  res['u_type']=='user':
                session['lid']=res['login_id']
                session['lg'] = 'lin'
                return '''<script>alert('successful');window.location="/userhome"</script>'''


        else:

            return '''<script>alert('not found');window.location="/"</script>'''
    else:
        return render_template("loginindex.html")

@app.route('/logout')
def logout():
    session.clear()
    session['lg']=""
    return redirect('/')


@app.route('/adminhome')
def home():
    if session['lg']=="lin":
        return render_template("ADMIN/admin_home.html")
    else:
        return redirect('/')


@app.route('/adminadd_category',methods=['GET','POST'])
def add_category():
    if session['lg'] == "lin":
        if request.method=="POST":
            category=request.form['textfield']
            db=Db()
            db.insert("insert into category VALUES ('','"+category+"')")
            return '''<script>alert('successful');window.location="/adminhome"</script>'''

        else:
            return render_template("ADMIN/category.html")
    else:
        return redirect('/')


@app.route('/adminviewcategory')
def view_category():
    if session['lg'] == "lin":
        db=Db()
        qry=db.select("select * from category")
        return render_template("ADMIN/view_category.html",data=qry)
    else:
        return redirect('/')

@app.route('/admindeletecategory/<id>')
def admindeletecategory(id):
    if session['lg'] == "lin":
                db=Db()
                qry=db.delete("delete from category where category_id = '"+id+"'")
                return '''<script>alert('successful');window.location="/adminviewcategory"</script>'''
    else:
        return redirect('/')


@app.route('/admin_viewworker')
def admin_viewworker():
    if session['lg'] == "lin":
            db = Db()
            qry = db.select("select * from worker,login where login.login_id=worker.user_id and u_type='pending' ")
            return render_template("ADMIN/view_worker.html",data=qry)
    else:
        return redirect('/')


@app.route('/approvingworker/<id>')
def approvingworker(id):
    if session['lg'] == "lin":
        db = Db()
        db.update("update login set u_type='worker' where login_id='"+str(id)+"'")
        return '''<script>alert('accepted');window.location="/admin_viewworker"</script>'''
    else:
        return redirect('/')


@app.route('/admindeleteworker/<id>')
def admindeleteworker(id):
    if session['lg'] == "lin":
        db=Db()
        qry=db.delete("delete from worker where user_id = '"+str(id)+"'")
        qry=db.delete("delete from login where login_id= '"+str(id)+"'")
        return '''<script>alert('successful');window.location="/admin_viewworker"</script>'''
    else:
        return redirect('/')


@app.route('/admin_viewapproved')
def admin_viewapproved():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("select * from login,worker where login.login_id=worker.user_id and login.u_type='worker' ")
        return render_template("ADMIN/apprvd_workers.html",data=qry)
    else:
        return redirect('/')


@app.route('/admin_viewuser')
def admin_viewuser():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("select * from user")
        return render_template("ADMIN/VIEW_USER.html",data=qry)
    else:
        return redirect('/')


@app.route('/admin_viewrating')
def admin_viewrating():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("select * from ratings_and_reviews,worker,user where ratings_and_reviews.worker_id=worker.user_id and ratings_and_reviews.user_id=user.user_id")
        return render_template("ADMIN/view_review.html",data=qry)
    else:
        return redirect('/')


@app.route('/admin_sendnotification',methods=['GET','POST'])
def admin_sendnotification():
    if session['lg'] == "lin":
        if request.method=="POST":
            notification=request.form['textarea']
            db=Db()
            db.insert("insert into notification VALUES ('','" +notification+ "',curdate())")
            return '''<script>alert('successful');window.location="/adminhome"</script>'''
        else:
            return render_template("ADMIN/Send_notification.html")
    else:
        return redirect('/')


@app.route('/admin_viewcomplaint')
def admin_viewcomplaint():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("select * from user,complaint_and_reply where user.user_id=complaint_and_reply.cuser_id and reply='pending' ")
        return render_template("ADMIN/view_COMPLAINT.html",data=qry)
    else:
        return redirect('/')


@app.route('/admin_replycomplaint/<id>',methods=['GET','POST'])
def admin_replycomplaint(id):
    if session['lg'] == "lin":
        if request.method=="POST":
            db=Db()
            reply=request.form['textarea']
            db.update("update complaint_and_reply set reply='"+reply+"',reply_date=curdate() where complaint_id='"+str(id)+"' ")
            return '''<script>alert('reply sending');window.location="/admin_viewcomplaint"</script>'''
        else:
            return render_template("ADMIN/reply_COMPLAINT.html")
    else:
        return redirect('/')


@app.route('/admin_viewfeedack')
def admin_viewfeedback():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("select * from user,feedback where user.user_id=feedback.f_uid ")
        return render_template("ADMIN/view_feedback.html",data=qry)
    else:
        return redirect('/')

##############################

@app.route('/worker_registr',methods=['get','post'])
def worker_registr():
    if request.method=="POST":
        name=request.form['textfield']
        house_name=request.form['textfield2']
        place=request.form['textfield3']
        post=request.form['textfield4']
        pin=request.form['textfield5']
        age=request.form['textfield6']
        photo=request.files['fileField']
        date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(r"C:\Users\91956\onlineelection\static\pic//"+date+'.jpg')
        ss="/static/pic/"+date+'.jpg'
        phone_number=request.form['textfield7']
        category=request.form['select']
        experience=request.form['textfield9']
        gender=request.form['RadioGroup1']
        email=request.form['textfield11']
        password=random.randint(0000,9999)
        db = Db()
        ss=db.selectOne("select * from login where username='"+email+"'")
        if ss is not None:
            return '''<script>alert('username already exists');window.location="/worker_registr"</script>'''
        qry = db.insert("insert into login VALUES ('','"+email+"','"+str(password)+"','pending')")
        db.insert("insert into worker VALUES ('"+str(qry)+"','"+name+"','"+house_name+"','"+place+"','"+post+"','"+pin+"','"+age+"','"+str(ss)+"','"+phone_number+"','"+category+"','"+experience+"','"+gender+"','"+email+"')")
        return '''<script>alert('REGISTERED SUCCESFULLY');window.location="/"</script>'''
    else:
        return render_template("WORKER/user_reg.html")


@app.route('/workerhome')
def workerhome():
    if session['lg'] == "lin":
            return render_template("WORKER/worker_home.html")
    else:
        return redirect('/')

@app.route('/workerviewreview')
def workerviewreview():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("select * from ratings_and_reviews,user where user.user_id=ratings_and_reviews.user_id ")
        return render_template("WORKER/wview_review.html",data=qry)
    else:
        return redirect('/')


@app.route('/workerviewnotification')
def workerviewnotification():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("select * from notification ")
        return render_template("WORKER/view_notification.html",data=qry)
    else:
        return redirect('/')


@app.route('/workerviewwork')
def workerviewwork():
    if session['lg'] == "lin":
        db = Db()
        qry = db.select("select * from work_request,user,service where work_request.user_ID=user.user_id and work_request.Service_id=service.service_id and work_request.status='pending'")
        return render_template("WORKER/work_request.html",data=qry)
    else:
        return redirect('/')


@app.route('/workapproving/<id>')
def workapproving(id):
    if session['lg'] == "lin":
        db = Db()
        db.update("update work_request set status='accepted' where Service_id='"+str(id)+"'")
        return '''<script>alert('accepted');window.location="/workerviewwork"</script>'''
    else:
        return redirect('/')


@app.route('/rejectwork/<id>')
def rejectwork(id):
    if session['lg'] == "lin":
        db=Db()
        qry=db.delete("delete from work_request where Service_id = '"+str(id)+"'")
        return '''<script>alert('successful');window.location="/workerviewwork"</script>'''
    else:
        return redirect('/')


@app.route('/workereditprofile')
def workereditprofile():
    if session['lg'] == "lin":
        db = Db()
        wid=session['lid']
        qry = db.selectOne("select * from worker where  user_id='"+str(wid)+"'")
        return render_template("WORKER/update_worker.html",data=qry)
    else:
        return redirect('/')


@app.route('/workerupdate/<id>',methods=['post'])
def workerupdate(id):
    if session['lg'] == "lin":
            name=request.form['textfield']
            house_name=request.form['textfield2']
            place=request.form['textfield3']
            post=request.form['textfield4']
            pin=request.form['textfield5']
            age=request.form['textfield6']
            photo=request.files['fileField']
            date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            photo.save(r"C:\Users\91956\onlineelection\static\pic//"+date+'.jpg')
            ss="/static/pic/"+date+'.jpg'
            phone_number=request.form['textfield7']
            category=request.form['select']
            experience=request.form['textfield9']
            gender=request.form['RadioGroup1']
            email=request.form['textfield11']
            password=random.randint(0000,9999)
            db = Db()
            if request.files!=None:
                if photo.filename!="":
                        db.update("update worker set name='"+name+"',home ='"+house_name+"',place='"+place+"',post='"+post+"',pin='"+pin+"',age='"+age+"',photo='"+str(ss)+"',phone_number='"+phone_number+"',category='"+category+"',experience='"+experience+"',gender='"+gender+"',email='"+email+"' where user_id='"+str(id)+"''' ")
                        return '''<script>alert('UPDATED SUCCESFULLY');window.location="/workereditprofile"</script>'''
                else:
                    db.update("update worker set name='" + name + "',home ='" + house_name + "',place='" + place + "',post='" + post + "',pin='" + pin + "',age='" + age + "',phone_number='" + phone_number + "',category='" + category + "',experience='" + experience + "',gender='" + gender + "',email='" + email + "' where user_id='" + str(id) + "''' ")
                    return '''<script>alert('UPDATED SUCCESFULLY');window.location="/workereditprofile"</script>'''
            else:
                db.update("update worker set name='" + name + "',home ='" + house_name + "',place='" + place + "',post='" + post + "',pin='" + pin + "',age='" + age + "',phone_number='" + phone_number + "',category='" + category + "',experience='" + experience + "',gender='" + gender + "',email='" + email + "' where user_id='" + str(id) + "''' ")
                return '''<script>alert('UPDATED SUCCESFULLY');window.location="/workereditprofile"</script>'''
    else:
        return redirect('/')


@app.route('/workerservice',methods=['post','get'])
def  workerservice():
    if session['lg'] == "lin":
        if request.method=="POST":
           service_type=request.form['textfield']
           charges=request.form['textfield3']
           lid=session['lid']
           db = Db()
           db.insert("insert into service VALUES ('','" + service_type + "','"+charges+"','"+str(lid)+"')")
           return '''<script>alert('added succesfully');window.location="/workerhome"</script>'''
        else:
           return render_template("WORKER/service.html")
    else:
        return redirect('/')

@app.route('/workerupdatestatus')
def workerupdatestatus():
    if session['lg'] == "lin":
        lid = session['lid']
        print(lid)
        db = Db()
        qry = db.select("select * from user,work_request,service where user.user_id=work_request.user_ID and work_request.Service_id=service.service_id and service.worker_id='"+str(lid)+"' and status='accepted'")
        return render_template("WORKER/statusupdate.html",data=qry)
    else:
        return redirect('/')

@app.route('/workcompleting/<id>')
def workcompleting(id):
    if session['lg'] == "lin":
        db = Db()
        db.update("update work_request set status='completed' where Service_id='"+str(id)+"'")
        return '''<script>alert('updated succesfully');window.location="/workerupdatestatus"</script>'''
    else:
        return redirect('/')

@app.route('/workeracceptedwork')
def workeracceptedwork():
    if session['lg'] == "lin":
        lid=session['lid']
        db = Db()
        qry = db.select("select * from user,work_request,service where user.user_id=work_request.user_ID and work_request.Service_id=service.service_id and service.worker_id='"+str(lid)+"' and status='completed'")
        return render_template("WORKER/accepted_work.html",data=qry)
    else:
        return redirect('/')
@app.route('/workerchangingpassword',methods=['post','get'])
def workerchangingpassword():
    if session['lg'] == "lin":
        if request.method=='POST':
            current_password=request.form['textfield']
            new_password=request.form['textfield2']
            confirm_password=request.form['textfield3']
            db = Db()
            lid = session['lid']
            print(lid)
            res=db.selectOne("select * from login where login_id='" + str(lid) + "' ")
            if current_password==str(res['password']):
                if new_password ==  confirm_password:
                    db.update("update login set password = '"+new_password+"' where login_id = '"+str(lid)+"'")
                    return  '''<script>alert('updated succesfully');window.location="/"</script>'''
                else:
                    return '''<script>alert('Password Does not match');window.location="/workerchangingpassword"</script>'''
            else:
                return '''<script>alert('incorrect password');window.location="/workerchangingpassword"</script>'''
        else:
              return render_template("WORKER/password.html")
    else:
        return redirect('/')


@app.route('/chat')
def chat():
        return render_template("WORKER/chat.html")


@app.route('/company_staff_chat', methods=['post'])
def company_staff_chat():
        # if session['ln'] == "oo":
        db = Db()
        # a = session['lid']
        # print(a)
        q = "select * from user"
        res = db.select(q)
        print(res)
        return jsonify(status='ok',data=res)
        # v={}
        # if len(res)>0:
        #     v["status"]="ok"
        #     v['data']=res
        # else:
        #     v["status"]="error"
        #
        # rq=demjson.encode(v)
        # print(rq)
        # return rq


@app.route('/chatsnd', methods=['post'])
def chatsnd():
        db = Db()
        c = session['lid']
        b = request.form['n']
        print(b)
        m = request.form['m']
        q2 = "insert into chat values(null,'" + str(c) + "','" + str(b) + "','" + m + "',now())"
        res = db.insert(q2)
        # v = {}
        # if int(res) > 0:
        #     v["status"] = "ok"
        #
        # else:
        #     v["status"] = "error"
        #
        # r = demjson.encode(v)
        v = jsonify(status='ok', data=res)
        return v


@app.route('/chatrply', methods=['post'])
def chatrply():
        c = session['lid']
        b = request.form['n']
        t = Db()
        qry2 = "select * from chat ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)
        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id']=c
        else:
            v["status"] = "error"
        # rw = demjson.encode(v)
        rw = jsonify(v)
        return rw
        v = jsonify(status='ok', data=res, id=c)
        return v


#############################################################

# @app.route('/user_rgstr',methods=['get','post'])
# def user_rgstr():
#     if request.method == "POST":
#             name=request.form['textfield']
#             house_name=request.form['textfield5']
#             place=request.form['textfield6']
#             post=request.form['textfield7']
#             pin=request.form['textfield8']
#             email=request.form['textfield2']
#             age=request.form['textfield3']
#             gender=request.form['RadioGroup1']
#             photo = request.files['fileField']
#             date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
#             photo.save(r"C:\Users\thasn\PycharmProjects\onlineelection\static\userpic\\" + date + ".jpg")
#             ss = "/static/userpic/" + date + ".jpg"
#             phone_number=request.form['textfield4']
#             password = random.randint(0000, 9999)
#             db = Db()
#             qry = db.insert("insert into login VALUES ('','" + email + "','" + str(password) + "','user')")
#             db.insert("insert into user VALUES ('"+str(qry)+"','"+name+"','"+house_name+"','"+place+"','"+post+"','"+pin+"','"+age+"','"+email+"','"+gender+"','"+str(ss)+"','"+phone_number+"')")
#             return '''<script>alert('REGISTERED SUCCESFULLY');window.location="/"</script>'''
#     else:
#          return render_template("user/add_user.html")
#
# @app.route('/userupdate/<id>',methods=['post'])
# def userupdate(id):
#
#     if request.method == "POST":
#         name=request.form['textfield']
#         house_name=request.form['textarea']
#         place=request.form['textfield5']
#         post=request.form['textfield6']
#         pin=request.form['textfield7']
#         email=request.form['textfield2']
#         age=request.form['textfield3']
#         photo = request.files['fileField']
#         date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
#         photo.save(r"C:\Users\thasn\PycharmProjects\onlineelection\static\userpic\\" + date + '.jpg')
#         ss = "/static/userpic/" + date + '.jpg'
#         phone_number = request.form['textfield4']
#         db = Db()
#         if request.files!=None:
#             if photo.filename!="":
#                 db.update("update user set u_name='"+name+"',hname='"+house_name+"',place='"+place+"',post='"+post+"',pin='"+pin+"',email='"+email+"',age='"+age+"',photo='"+str(ss)+"',phone_number='"+phone_number+"' where user_id='"+str(id)+"''' ")
#                 return '''<script>alert('UPDATED SUCCESFULLY');window.location="/usereditprofile"</script>'''
#
#             else:
#                 db.update("update user set u_name='"+name+"',hname='"+house_name+"',place='"+place+"',post='"+post+"',pin='"+pin+"',email='"+email+"',age='"+age+"',phone_number='"+phone_number+"' where user_id='"+str(id)+"''' ")
#                 return '''<script>alert('UPDATED SUCCESFULLY');window.location="/usereditprofile"</script>'''
#
#         else:
#             db.update( "update user set u_name='" + name + "',hname='" + house_name + "',place='" + place + "',post='" + post + "',pin='" + pin + "',email='" + email + "',age='" + age + "',phone_number='" + phone_number + "' where user_id='" + str(id) + "''' ")
#             return '''<script>alert('UPDATED SUCCESFULLY');window.location="/usereditprofile"</script>'''
#
#
#
# @app.route('/usereditprofile')
# def usereditprofile():
#     db = Db()
#     uid=session['lid']
#     qry = db.selectOne("select * from user where  user_id='"+str(uid)+"'")
#     return render_template("user/edit_user.html",data=qry)
#
# @app.route('/userhome')
# def userhome():
#  return render_template("user/uhomepage.html")
#
# @app.route('/userchangingpassword',methods=['post','get'])
# def userchangingpassword():
#     if request.method=='POST':
#         current_password=request.form['textfield']
#         new_password=request.form['textfield2']
#         confirm_password=request.form['textfield3']
#         db = Db()
#         lid = session['lid']
#         print(lid)
#
#         res=db.selectOne("select * from login where login_id='" + str(lid) + "' ")
#         if current_password==str(res['password']):
#
#             if new_password ==  confirm_password:
#                 db.update("update login set password = '"+new_password+"' where login_id = '"+str(lid)+"'")
#                 return  '''<script>alert('updated succesfully');window.location="/"</script>'''
#
#             else:
#                 return '''<script>alert('Password Does not match');window.location="/userchangingpassword+"</script>'''
#
#
#         else:
#             return '''<script>alert('incorrect password');window.location="/userchangingpassword"</script>'''
#     else:
#           return render_template("user/password.html")
#
# @app.route('/userviewnotification')
# def userviewnotification():
#     db = Db()
#     qry = db.select("select * from notification ")
#     return render_template("user/view_notification.html",data=qry)
#
#
# @app.route('/usersendcomplaint',methods=['GET','POST'])
# def usersendcomplaint():
#     if request.method=="POST":
#         complaints=request.form['textarea']
#         db=Db()
#         lid = session['lid']
#         db.insert("insert into complaint_and_reply VALUES ('','" + str(lid) + "','" +complaints+ "',curdate(),'pending','pending')")
#         return '''<script>alert('successful');window.location="/userhome"</script>'''
#
#     else:
#         return render_template("user/send_COMPLAINT.html")
#
# @app.route('/userviewcomplaint')
# def userviewcomplaint():
#     db = Db()
#     lid = session['lid']
#     qry = db.select("select * from complaint_and_reply WHERE cuser_id='"+str(lid)+"' ")
#     return render_template("user/replyview_COMPLAINT.html",data=qry)
#
#
#
# @app.route('/usersendfeedback',methods=['GET','POST'])
# def usersendfeedback():
#     if request.method=="POST":
#         notification=request.form['textarea']
#         db=Db()
#         db.insert("insert into notification VALUES ('','" +notification+ "',curdate())")
#         return '''<script>alert('successful');window.location="/adminhome"</script>'''
#
#     else:
#         return render_template("ADMIN/Send_notification.html")

# -----------------------------------------------------------------------------------------------------------------------
#                                             USER MODULE-ANDROID
# --------------------------------------------------------------------------------------------------------------------------------------------------


@app.route('/user_rgstr',methods=['post'])
def user_rgstr():
    if request.method == "POST":
            name=request.form['na']
            house_name=request.form['hname']
            place=request.form['place']
            post=request.form['post']
            pin=request.form['pin']
            dob=request.form['dob']
            email=request.form['email']
            phone=request.form['phone']
            password = request.form['passwd']
            pic = request.files['pic']
            date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            pic.save(r"C:\Users\91956\onlineelection\static\userpic\\" + date + ".jpg")
            ss = "/static/userpic/" + date + ".jpg"
            db = Db()
            ssw=db.selectOne("select * from login where username='"+email+"'")
            print(ssw)
            if ssw is not None:
                return jsonify(status="")
            else:
                qry = db.insert("insert into login VALUES ('','" + email + "','" + str(password) + "','user')")
                db.insert("insert into user VALUES ('" + str(qry) + "','" + name + "','" + house_name + "','" + place + "','" + post + "','" + pin + "','" + dob + "','" + email + "','" + phone + "','" + str(ss) + "','" + password + "')")
                return jsonify(status="ok")



@app.route('/and_login',methods=['post'])
def and_login():
    db=Db()
    username=request.form['u']
    password=request.form['p']
    print(usernamFe,password)
    result=db.selectOne("select * from login WHERE username='"+username+"' and password='"+password+"' ")
    res={}
    if result is not None:
        ss=db.selectOne("select * from user where user_id='"+str(result['login_id'])+"'")
        return jsonify(status = "ok" , type = result['u_type'],lid = result['login_id'],name=ss['u_name'],email=ss['email'])
    else:
        return jsonify(status="none")



@app.route('/and_sndcmplnt',methods=['post'])
def and_sndcmplnt():
    db=Db()
    complaint=request.form['comp']
    lid=request.form['id']
    result=db.insert("insert into complaint_and_reply values ('','"+lid+"','"+complaint+"',curdate(),'pending','pending') ")
    res={}
    if result is not None:
        return jsonify(status="ok")
    else:
        return jsonify(status="none")


@app.route('/and_feedback',methods=['post'])
def and_feedback():
    db=Db()
    feedback=request.form['feed']
    lid=request.form['id']
    result=db.insert("insert into feedback values ('','"+lid+"','"+feedback+"',curdate())")
    res={}
    if result is not None:
        return jsonify(status="ok")
    else:
        return jsonify(status="none")


@app.route('/and_view_profile',methods=['post'])
def and_view_profile():
    db=Db()
    lid=request.form['id']
    print(lid)
    result=db.selectOne("select * from user where user_id = '"+lid+"'")
    if result is not None:
        return jsonify(status="ok",data = result)
    else:
        return jsonify(status="none")
    return "ok"


# @app.route('/and_edit_profile',methods=['post'])
# def and_edit_profile():
    name=request.form['nm']
    # return "ok"
    # house_name=request.form['hm']
    # place=request.form['place']
    # post=request.form['post']
    # pin=request.form['pin']
    #
    #
    # photo = request.files['photo']
    # date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
    # photo.save(r"C:\Users\thasn\PycharmProjects\onlineelection\static\userpic\\" + date + '.jpg')
    # ss = "/static/userpic/" + date + '.jpg'
    # phone_number = request.form['phone_number']

    # print(name)



@app.route('/and_edit_profile',methods=['post'])
def and_edit_profile():
    db=Db()
    lid = request.form['id']
    name = request.form['nam']
    h = request.form['h_n']
    pl=request.form['plc']
    po=request.form['po']
    pin=request.form['pin']
    ph=request.form['ph']
    result=db.update("update user set u_name='"+name+"',hname='"+h+"',place='"+pl+"',post='"+po+"',pin='"+pin+"',phone_number='"+ph+"' where user_id='"+lid+"'")
    res = {}
    if result is not None:
        return jsonify(status="ok")
    else:
        return jsonify(status="none")


@app.route('/and_review_rating',methods=['post'])
def and_review_rating():
    db=Db()
    lid=request.form['id']
    rvw=request.form['review']
    result=db.insert("insert into ratings_and_reviews values ('','pending','"+rvw+"',curdate(),7,'"+lid+"') ")
    print(result)
    res={}
    if result is not None:
        return jsonify(status="ok",rid=result)
    else:
        return jsonify(status="none")


@app.route('/rating',methods=['post'])
def rating():
    db=Db()
    rid=request.form['rid']
    star=request.form['star']
    result=db.insert("update ratings_and_reviews set  rating='"+star+"' where rating_id='"+rid+"'")
    # print(result)
    res={}
    if result is not None:
        return jsonify(status="ok")
    else:
        return jsonify(status="none")


@app.route('/and_view_workers',methods=['post'])
def and_view_workers():
    db=Db()
    result=db.select("select * from worker")
    res={}
    if result:
        return jsonify(status="ok",data=result)
    else:
        return jsonify(status="none")


@app.route('/and_send_request',methods=['post'])
def and_send_request():
    db=Db()
    uid=request.form['uid']
    wid=request.form['wid']
    qry=db.selectOne("select * from work_request where user_ID='"+uid+"' and Service_id='"+wid+"' and date=curdate()")
    if qry:
        return jsonify(status="already")
    else:
        result=db.insert("insert into work_request values ('','"+uid+"','"+wid+"','','pending',curdate())")
        res={}
        if result is not None:
            return jsonify(status="ok")
        else:
            return jsonify(status="none")


@app.route('/and_view_request',methods=['post'])
def and_view_request():
    db=Db()
    lid = request.form['id']
    result=db.select("select *  from work_request,worker,service where work_request.Service_id=service.service_id and worker.user_id=service.worker_id and work_request.user_ID='"+lid+"'")
    res={}
    if result:
        return jsonify(status="ok",data=result)
    else:
        return jsonify(status="none")


@app.route('/and_publ_view_categ',methods=['post'])
def and_publ_view_categ():
    db=Db()
    result=db.select("select * from worker")
    res={}
    if result:
        return jsonify(status="ok", data=result)
    else:
        return jsonify(status="none")



@app.route('/and_publ_view_feed',methods=['post'])
def and_publ_view_feed():
    db=Db()
    result=db.select("select * from feedback,user where feedback.f_uid=user.user_id")
    res={}
    if result:
        return jsonify(status="ok", data=result)
    else:
        return jsonify(status="none")



@app.route('/and_publ_view_noti',methods=['post'])
def and_publ_view_noti():
    db=Db()
    result=db.select("select * from notification")
    res={}
    if result:
        return jsonify(status="ok", data=result)
    else:
        return jsonify(status="none")


@app.route('/complaint_and_reply',methods=['post'])
def complaint_and_reply():
    db=Db()
    lid = request.form['id']
    result=db.select("select *  from complaint_and_reply,user where user.user_id=complaint_and_reply.cuser_id and cuser_id""='"+lid+"'")
    res={}
    if result:
        return jsonify(status="ok",data=result)
    else:
        return jsonify(status="none")



@app.route('/in_message2',methods=['post'])
def in_message2():
    db=Db()
    lid = request.form['fid']
    toid = request.form['toid']
    message = request.form['msg']
    q2="insert into chat(from_id,to_id,message,date)values('"+lid+"','"+toid+"','"+message+"',curdate())"
    res = db.insert(q2)
    res1 = {}
    res1['status'] = "Inserted"
    return jsonify(status="ok")


@app.route('/view_message2',methods=['post'])
def view_message2():
    lid = request.form['fid']
    toid = request.form['toid']
    lastid = request.form['lastmsgid']
    print(lid,toid,lastid)
    db=Db()
    q2="select chat.* from chat where chat_id>'"+lastid+"' and ((from_id='"+lid+"' and to_id='"+toid+"') or (from_id='"+toid+"' and to_id='"+lid+"'))"
    res = db.select(q2)
    print(res)
    return jsonify(res1=res,status="ok")

#####################user chat


@app.route('/add_chat',methods=['post'])
def add_chat():
    db=Db()
    lid = request.form['lid']
    toid = request.form['toid']
    message = request.form['message']
    print(lid,toid)
    q2="insert into chat(from_id,to_id,message,date)values('"+lid+"','"+toid+"','"+message+"',curdate())"
    res = db.insert(q2)
    # res1 = {}
    # res1['status'] = "Inserted"
    return jsonify(status="Inserted")


@app.route('/view_chat',methods=['post'])
def view_chat():
    db=Db()
    lid = request.form['lid']
    toid = request.form['toid']
    lastid = request.form['lastid']
    print(lid,toid,lastid)
    q2="select chat.* from chat where chat_id>'"+lastid+"' and ((from_id='"+lid+"' and to_id='"+toid+"') or (from_id='"+toid+"' and to_id='"+lid+"'))"
    res = db.select(q2)
    print(res)
    # res1 = {}
    # res1['status'] = "ok"
    # res1['data'] = res
    return jsonify(status="ok",data=res)


@app.route('/view_staff',methods=['post'])
def view_chatcouncillor():
    db=Db()
    lid = request.form['lid']
    print(lid)
    qry = db.select("select * from worker,login where login.login_id=worker.user_id and login.u_type='worker'")
    print(qry)
    # cid = qry['stud_course_id']
    # y = qry['batch']
    # q = db.select("select * from subect_alloc,staff,subject,suballoctocourse where  suballoctocourse.suballoccourseid=subect_alloc.csuballocid and suballoctocourse.ssubid=subject.sub_id and staff.Staff_id=subect_alloc.staff_name and suballoctocourse.scid='"+str(cid)+"' group by staff.Staff_id ")
    # # print(q, cid)
    # res1 = {}
    # res1['status'] = "ok"
    # res1['data'] = q
    return jsonify(status="ok",data=qry)


if __name__=='__main__':
            app.run(host="0.0.0.0")
