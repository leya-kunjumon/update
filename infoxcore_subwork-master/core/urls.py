
from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from base_app import views
from cal import views as calviews



urlpatterns = [
    re_path('admin/', admin.site.urls),
    
    re_path(r'^$', views.login, name='login'),
    
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path(r'^logout4/$', views.logout4, name='logout4'),
    re_path(r'^logout2/$', views.logout2, name='logout2'),
    re_path(r'^logout3/$', views.logout3, name='logout3'),


    ########################################## Training Manager #######################################################
    re_path(r'^Dashboard/$', views.Dashboard, name='Dashboard'),
    re_path(r'^Statustable/(?P<id>\d+)$',
            views.statusTable, name="statusTable"),
    re_path(r'^trainee_applyleave_cards/$',
            views.trainee_applyleave_cards, name='trainee_applyleave_cards'),
    re_path(r'^trainee_appliedleave/$', views.trainee_appliedleave,
            name='trainee_appliedleave'),

    re_path(r'^Newtrainees/$', views.Newtrainees, name='Newtrainees'),
    re_path(r'^newtraineeesteam/$', views.newtraineeesteam,
            name='newtraineeesteam'),
    re_path(r'^new_team/$', views.new_team, name='new_team'),

    re_path(r'^new_team1/$', views.new_team1, name='new_team1'),
    re_path(r'^newteamcreate/$', views.newteamcreate, name='newteamcreate'),
    re_path(r'^teamdelete/$', views.teamdelete, name='teamdelete'),
    re_path(r'^teamupdate/$', views.teamupdate, name='teamupdate'),
    re_path(r'^submit/$', views.submit, name='submit'),
    re_path(r'^reportedissue/$', views.reportedissue, name='reportedissue'),
    re_path(r'^reportissuetrainers/$', views.reportissuetrainers,
            name='reportissuetrainers'),
    re_path(r'^trainerunsolvedissue/$', views.trainerunsolvedissue,
            name='trainerunsolvedissue'),
    re_path(r'^savetmreplaytrnr/$', views.savetmreplaytrnr,
            name='savetmreplaytrnr'),
    re_path(r'^trainersolvedissue/$', views.trainersolvedissue,
            name='trainersolvedissue'),
    re_path(r'^reportissuetrainees/$', views.reportissuetrainees,
            name='reportissuetrainees'),
    re_path(r'^traineesunsolved/$', views.traineesunsolved,
            name='traineesunsolved'),
    re_path(r'^savetmreplytrns/$', views.savetmreplytrns,
            name='savetmreplytrns'),
    re_path(r'^traineessolved/$', views.traineessolved, name='traineessolved'),
    re_path(r'^reportissue/$', views.reportissue, name='reportissue'),
    re_path(r'^reportedissuesub/$', views.reportedissuesub,

            name='reportedissuesub'),
    re_path(r'^Applyleave/$', views.Applyleave, name='Applyleave'),
    re_path(r'^trainers_leave/$', views.trainers_leave, name='trainers_leave'),
    re_path(r'^trainees_leave/$', views.trainees_leave, name='trainees_leave'),
    re_path(r'^trainer_leavestatus/$', views.trainer_leavestatus,
            name='trainer_leavestatus'),
    re_path(r'^trainees_leavestatus/$', views.trainees_leavestatus,
            name='trainees_leavestatus'),
    re_path(r'^Leave_rejected/$', views.Leave_rejected, name='Leave_rejected'),
    re_path(r'^Trainee_Leave_rejected/$', views.Trainee_Leave_rejected,
            name='Trainee_Leave_rejected'),
    re_path(r'^applyleavesub/$', views.applyleavesub, name='applyleavesub'),
    re_path(r'^Requestedleave/$', views.Requestedleave, name='Requestedleave'),
    re_path(r'^trainers_leavelist/$', views.trainers_leavelist,
            name='trainers_leavelist'),

    re_path(r'^approvedstatus/(?P<id>\d+)$',
            views.approvedstatus, name='approvedstatus'),
    re_path(r'^approvedstatus_trainee/(?P<id>\d+)$',
            views.approvedstatus_trainee, name='approvedstatus_trainee'),
    re_path(r'^trainees_leavelist/$', views.trainees_leavelist,
            name='trainees_leavelist'),
    re_path(r'^trainer_trainees_details/(?P<id>\d+)/$', views.trainer_trainees_details, name='trainer_trainees_details'),
    re_path(r'^Trainee/$', views.Trainee, name="Trainee"),
    re_path(r'^trainer/$', views.trainer, name='trainer'),
    re_path(r'^team1/(?P<id>\d+)$', views.team1, name='team1'),
    re_path(r'^current/(?P<id>\d+)$', views.current, name='current'),
    re_path(r'^task/(?P<id>\d+)$', views.task, name='task'),
    re_path(r'^Trainer_Current_Assigned/(?P<id>\d+)$',
            views.Trainer_Current_Assigned, name='Trainer_Current_Assigned'),
    re_path(r'^Trainer_Currenttrainee/(?P<id>\d+)$',
            views.Trainer_Currenttrainee, name='Trainer_Currenttrainees'),
    re_path(r'^Empdetails/(?P<id>\d+)$', views.Empdetails, name='Empdetails'),
    re_path(r'^Trainer_Previousattendance/(?P<id>\d+)$',
            views.Trainer_Previousattendance, name='Trainer_Previousattendance'),
    re_path(r'^List/(?P<id>\d+)$', views.List, name='List'),
    re_path(r'^task1/(?P<id>\d+)$', views.task1, name='task1'),
    re_path(r'^tdetails/(?P<id>\d+)$', views.tdetails, name='tdetails'),
    re_path(r'^prteam/(?P<id>\d+)$', views.Previous, name='prteam'),
    re_path(r'^prtask/(?P<id>\d+)$', views.Previous_Task, name='prtask'),
    re_path(r'^prass/(?P<id>\d+)$', views.Previous_Assigned, name='prass'),
    re_path(r'^Trainer_Previous_Trainees/(?P<id>\d+)$',
            views.Trainer_Previous_Trainees, name='Trainer_Previous_Trainees'),
    re_path(r'^PEmpdetails/(?P<id>\d+)$',
            views.PEmpdetails, name='PEmpdetails'),
    re_path(r'^PAttendance/(?P<id>\d+)$',
            views.PAttendance, name='PAttendance'),
    re_path(r'^PList/(?P<id>\d+)$', views.PList, name='PList'),
    re_path(r'^Ptask1/(?P<id>\d+)$', views.Ptask1, name='Ptask1'),
    re_path(r'^Ptdetails/(?P<id>\d+)$', views.Ptdetails, name='Ptdetails'),
    re_path(r'^traineedetails/(?P<id>\d+)$',
            views.traineedetails, name="traineedetails"),



    ########################################## Trainer Module #########################################################

    re_path(r'^trainer_dashboard/$', views.trainer_dashboard,
            name='trainer_dashboard'),


    re_path(r'^trainer_applyleave/$', views.trainer_applyleave,
            name='trainer_applyleave'),
    re_path(r'^trainer_applyleave_form/$', views.trainer_applyleave_form,
            name='trainer_applyleave_form'),
    re_path(r'^trainer_traineesleave_table/$',
            views.trainer_traineesleave_table, name='trainer_traineesleave_table'),


    re_path(r'^trainer_reportissue/$', views.trainer_reportissue,
            name='trainer_reportissue'),
    re_path(r'^trainer_reportissue_form/$',
            views.trainer_reportissue_form, name='trainer_reportissue_form'),
    re_path(r'^trainer_reportedissue_table/$',
            views.trainer_reportedissue_table, name='trainer_reportedissue_table'),
    re_path(r'^trainer_myreportissue_table/$',
            views.trainer_myreportissue_table, name='trainer_myreportissue_table'),
    re_path(r'^savereplaytnee/(?P<id>\d+)$',
            views.savereplaytnee, name='savereplaytnee'),


    re_path(r'^trainer_topic/$', views.trainer_topic, name='trainer_topic'),
    re_path(r'^trainer_addtopic/$', views.trainer_addtopic,
            name='trainer_addtopic'),
    re_path(r'^trainer_viewtopic/$', views.trainer_viewtopic,
            name='trainer_viewtopic'),
    re_path(r'^trainer_attendance/$', views.trainer_attendance,
            name='trainer_attendance'),
    re_path(r'^trainer_attendance_trainer/$',
            views.trainer_attendance_trainer, name='trainer_attendance_trainer'),
    re_path(r'^trainer_attendance_trainer_viewattendance/$',
            views.trainer_attendance_trainer_viewattendance, name='trainer_attendance_trainer_viewattendance'),
    re_path(r'^trainer_attendance_trainer_viewattendancelist/$',
            views.trainer_attendance_trainer_viewattendancelist, name='trainer_attendance_trainer_viewattendancelist'),
    re_path(r'^trainer_attendance_trainees/$',
            views.trainer_attendance_trainees, name='trainer_attendance_trainees'),

    re_path(r'^attendance_tm/$', views.attendance_tm, name='attendance_tm'),
    re_path(r'^Trainees_Calendar/$', views.Trainees_Calendar,
            name='Trainees_Calendar'),
    re_path(r'^Trainees_Attendancetable/$',
            views.Trainees_Attendancetable, name='Trainees_Attendancetable'),
    re_path(r'^Trainers_Calendar/$', views.Trainers_Calendar,
            name='Trainers_Calendar'),
    re_path(r'^Trainers_Attendancetable/$',
            views.Trainers_Attendancetable, name='Trainers_Attendancetable'),


    re_path(r'^trainer_team/$', views.trainer_team, name='trainer_team'),
    re_path(r'^trainer_currentteam/$', views.trainer_currentteam,
            name='trainer_currentteam'),
    re_path(r'^attenperform$', views.attenperform, name='attenperform'),
    re_path(r'^trainer_currenttrainees/(?P<id>\d+)$',
            views.trainer_currenttrainees, name='trainer_currenttrainees'),
    re_path(r'^trainer_currenttraineesdetails/(?P<id>\d+)$',
            views.trainer_currenttraineesdetails, name='trainer_currenttraineesdetails'),
    re_path(r'^trainer_currentattentable/(?P<id>\d+)$',
            views.trainer_currentattentable, name='trainer_currentattentable'),
    re_path(r'^trainer_currentperform/(?P<id>\d+)$',
            views.trainer_currentperform, name='trainer_currentperform'),
    re_path(r'^trainer_currentattenadd/(?P<id>\d+)$',
            views.trainer_currentattenadd, name='trainer_currentattenadd'),
    re_path(r'^trainer_previousteam/$', views.trainer_previousteam,
            name='trainer_previousteam'),
    re_path(r'^trainer_previoustrainees/(?P<id>\d+)$',
            views.trainer_previoustrainees, name='trainer_previoustrainees'),
    re_path(r'^trainer_previoustraineesdetails/(?P<id>\d+)$',
            views.trainer_previoustraineesdetails, name='trainer_previoustraineesdetails'),
    re_path(r'^trainer_previousattentable/(?P<id>\d+)$',
            views.trainer_previousattentable, name='trainer_previousattentable'),
    re_path(r'^trainer_previousperfomtable/(?P<id>\d+)$',
            views.trainer_previousperfomtable, name='trainer_previousperfomtable'),
    re_path(r'^trainer_current_attendance/(?P<id>\d+)$',
            views.trainer_current_attendance, name='trainer_current_attendance'),
    re_path(r'^trainer_current_attendance_view/(?P<id>\d+)$',
            views.trainer_current_attendance_view, name='trainer_current_attendance_view'),



    re_path(r'^trainer_Task/$', views.trainer_Task, name="trainer_Task"),
    re_path(r'^trainer_teamlist/$', views.trainer_teamlistpage,
            name="traineer_teamlistpage"),
    re_path(r'^trainer_taskfor/(?P<id>\d+)$',
            views.trainer_taskpage, name="traineer_taskpage"),
    re_path(r'^trainer_givetask/(?P<id>\d+)$',
            views.trainer_givetask, name="traineer_givetask"),
    re_path(r'^trainer_taskgiven/(?P<id>\d+)$',
            views.trainer_taskgivenpage, name="traineer_taskgivenpage"),

    re_path(r'^attendance/$', views.Attendance, name='attendance'),
    re_path(r'^trainees_attendance_viewattendance/$',
            views.trainees_attendance_viewattendance, name='trainees_attendance_viewattendance'),
    re_path(r'^trainees_attendance_viewattendancelist/$',
            views.trainees_attendance_viewattendancelist, name='trainees_attendance_viewattendancelist'),

    re_path(r'^trainer_taska/$', views.trainer_taska, name='trainer_taska'),
    re_path(r'^trainer_task_completed_teamlist/$',
            views.trainer_task_completed_teamlist, name='trainer_task_completed_teamlist'),
    re_path(r'^trainer_task_completed_team_tasklist/$',
            views.trainer_task_completed_team_tasklist, name='trainer_task_completed_team_tasklist'),
    re_path(r'^trainer_task_previous_teamlist/$',
            views.trainer_task_previous_teamlist, name='trainer_task_previous_teamlist'),
    re_path(r'^trainer_task_previous_team_tasklist/(?P<id>\d+)$',
            views.trainer_task_previous_team_tasklist, name='trainer_task_previous_team_tasklist'),

    re_path(r'^trainer_trainees/$', views.trainer_trainees,
            name='trainer_trainees'),

    re_path(r'^trainer_current_trainees/$',
            views.trainer_current_trainees, name='trainer_current_trainees'),
            
    re_path(r'^trainer_paymentlist/$', views.trainer_paymentlist, name="trainer_paymentlist"),
    re_path(r'^trainer_payment_viewslip/(?P<id>\d+)/(?P<tid>\d+)/$', views.trainer_payment_viewslip, name="trainer_payment_viewslip"),
    re_path(r'^trainer_payment_print/(?P<id>\d+)/(?P<tid>\d+)/$', views.trainer_payment_print,name='trainer_payment_print'),


    ###################################     NEW         #######################################

    re_path(r'^trainer_attendance_trainees_viewattendance/$',
            views.trainer_attendance_trainees_viewattendance, name='trainer_attendance_trainees_viewattendance'),
    re_path(r'^trainer_attendance_trainees_viewattendancelist/$',
            views.trainer_attendance_trainees_viewattendancelist, name='trainer_attendance_trainees_viewattendancelist'),
    re_path(r'^trainer_attendance_trainees_addattendance/$',
            views.trainer_attendance_trainees_addattendance, name='trainer_attendance_trainees_addattendance'),


    re_path(r'^trainer_applyleave_cards/$',
            views.trainer_applyleave_cards, name='trainer_applyleave_cards'),

    re_path(r'^trainer_appliedleave/$', views.trainer_appliedleave,
            name='trainer_appliedleave'),


    ########################################## Trainee Module #########################################################

    re_path(r'^trainee_dashboard_trainee/$',
            views.trainee_dashboard_trainee, name='trainee_dashboard_trainee'),

    re_path(r'^trainee_task/$', views.trainee_task, name='trainee_task'),
    re_path(r'^trainee_task_list/$', views.trainee_task_list,
            name='trainee_task_list'),
    re_path(r'^trainee_task_details/(?P<id>\d+)$', views.trainee_task_details,
            name='trainee_task_details'),
    re_path(r'^trainee_completed_taskList/$',
            views.trainee_completed_taskList, name='trainee_completed_taskList'),

    re_path(r'^trainee_reported_issue/$', views.trainee_reported_issue,
            name='trainee_reported_issue'),
    re_path(r'^trainee_report_reported/$', views.trainee_report_reported,
            name='trainee_report_reported'),
    re_path(r'^trainee_report_issue/$', views.trainee_report_issue,
            name='trainee_report_issue'),
    re_path(r'^trainee_applyleave_form/$', views.trainee_applyleave_form,
            name='trainee_applyleave_form'),

    re_path(r'^trainee_topic/$', views.trainee_topic, name='trainee_topic'),
    re_path(r'^trainee_currentTopic/$', views.trainee_currentTopic,
            name='trainee_currentTopic'),
    re_path(r'^save_trainee_review/$', views.save_trainee_review,
            name='save_trainee_review'),
    re_path(r'^trainee_previousTopic/$', views.trainee_previousTopic,
            name='trainee_previousTopic'),
    ###################################  Account & changepassword  #########################################


    re_path(r'^account_trainer/$', views.account_trainer,
            name='account_trainer'),
    re_path(r'^imagechange/$', views.imagechange, name='imagechange'),
    re_path(r'^changepassword_trainer/$', views.changepassword_trainer,
            name='changepassword_trainer'),


    re_path(r'^account_tr_mg/$', views.account_tr_mg, name='account_tr_mg'),
    re_path(r'^imagechange_tr/$', views.imagechange_tr, name='imagechange_tr'),
    re_path(r'^changepassword_tr_mg/$', views.changepassword_tr_mg,
            name='changepassword_tr_mg'),


    re_path(r'^account_trainees/$', views.account_trainees,
            name='account_trainees'),
    re_path(r'^imagechange_trainees/$', views.imagechange_trainees,
            name='imagechange_trainees'),
    re_path(r'^changepassword_trainees/$',
            views.changepassword_trainees, name='changepassword_trainees'),

    ############################################# Amal #############################################################
    
    re_path(r'^Admlogout/$', views.Admlogout, name='Admlogout'),
    re_path(r'^Mnlogout/$', views.Mnlogout, name='Mnlogout'),
    
    # ***************************Admin and Manager Account setting***********************************
    
    re_path(r'^BRadmin_projects_details/$', views.BRadmin_projects_details, name='BRadmin_projects_details'),
    
    re_path(r'^BRadmin_workstatus/$', views.BRadmin_workstatus, name='BRadmin_workstatus'),
    
    re_path(r'^BRadmin_emp_ajax/$', views.BRadmin_emp_ajax, name='BRadmin_emp_ajax'),
    re_path(r'^BRadmin_designations/$', views.BRadmin_designations, name='BRadmin_designations'),
    re_path(r'^BRadmin_accsetting/$', views.BRadmin_accsetting, name='BRadmin_accsetting'),
    re_path(r'^BRadmin_accsettingimagechange/(?P<id>\d+)/$', views.BRadmin_accsettingimagechange, name='BRadmin_accsettingimagechange'),
    re_path(r'^MAN_accsetting/$', views.MAN_accsetting, name='MAN_accsetting'),
    re_path(r'^MAN_accsettingimagechange/(?P<id>\d+)/$', views.MAN_accsettingimagechange, name='MAN_accsettingimagechange'),
    
    # ***************************Admin and Manager Change password***********************************
    
    re_path(r'^BRadmin_changepwd/$', views.BRadmin_changepwd, name='BRadmin_changepwd'),
    re_path(r'^MAN_changepwd/$', views.MAN_changepwd, name='MAN_changepwd'),
    
    # ***************************anandu***********************************
    re_path(r'^MAN_profiledash/$', views.MAN_profiledash, name='MAN_profiledash'),
    re_path(r'^MAN_index/$', views.MAN_index, name='MAN_index'),
    re_path(r'^MAN_employees/$', views.MAN_employees, name='MAN_employees'),
    re_path(r'^MAN_python/(?P<id>\d+)/$', views.MAN_python, name='MAN_python'),
    re_path(r'^MAN_projectman/(?P<id>\d+)/(?:(?P<did>\d+))?',
            views.MAN_projectman, name='MAN_projectman'),
    re_path(r'^MAN_proname/(?P<id>\d+)/$',
            views.MAN_proname, name='MAN_proname'),
    re_path(r'^MAN_proinvolve/(?P<id>\d+)/$',
            views.MAN_proinvolve, name='MAN_proinvolve'),
    re_path(r'^MAN_promanatten/(?P<id>\d+)/$',
            views.MAN_promanatten, name='MAN_promanatten'),
    re_path(r'^MAN_promanattendsort/(?P<id>\d+)/$',
            views.MAN_promanattendsort, name='MAN_promanattensort'),

    re_path(r'^BRadmin_profiledash/$', views.BRadmin_profiledash,
            name='BRadmin_profiledash'),
    re_path(r'^BRadmin_index/$', views.BRadmin_index, name='BRadmin_index'),
    re_path(r'^BRadmin_employees/$', views.BRadmin_employees,
            name='BRadmin_employees'),
    re_path(r'^BRadmin_python/(?P<id>\d+)/$',
            views.BRadmin_python, name='BRadmin_python'),
    re_path(r'^BRadmin_projectman/(?P<id>\d+)/(?:(?P<did>\d+))?',
            views.BRadmin_projectman, name='BRadmin_projectman'),
    re_path(r'^BRadmin_proname/(?P<id>\d+)/$',
            views.BRadmin_proname, name='BRadmin_proname'),
    re_path(r'^BRadmin_proinvolve/(?P<id>\d+)/$',
            views.BRadmin_proinvolve, name='BRadmin_proinvolve'),
    re_path(r'^BRadmin_promanatten/(?P<id>\d+)/$',
            views.BRadmin_promanatten, name='BRadmin_promanatten'),
    re_path(r'^BRadmin_promanattendsort/(?P<id>\d+)/$',
            views.BRadmin_promanattendsort, name='BRadmin_promanattensort'),


    # ********************praveen********************************
    re_path(r'^BRadmin_trainerstable/(?P<did>\d+)/$', views.BRadmin_trainerstable,
            name='BRadmin_trainerstable'),
    re_path(r'^BRadmin_Training/(?P<id>\d+)/$',
            views.BRadmin_Training, name='BRadmin_Training'),
    re_path(r'^BRadmin_trainingteam1/(?P<id>\d+)/$',
            views.BRadmin_trainingteam1, name='BRadmin_trainingteam1'),
    re_path(r'^BRadmin_traineestable/(?P<id>\d+)/$',
            views.BRadmin_traineestable, name='BRadmin_traineestable'),
    re_path(r'^BRadmin_trainingprofile/(?P<id>\d+)/$',
            views.BRadmin_trainingprofile, name='BRadmin_trainingprofile'),
    re_path(r'^BRadmin_completedtasktable/(?P<id>\d+)/$',
            views.BRadmin_completedtasktable, name='BRadmin_completedtasktable'),
    re_path(r'^BRadmin_topictable/(?P<id>\d+)/$',
            views.BRadmin_topictable, name='BRadmin_topictable'),

    re_path(r'^MAN_trainerstable/(?P<id>\d+)$', views.MAN_trainerstable,
            name='MAN_trainerstable'),
    re_path(r'^MAN_Training/(?P<id>\d+)/$',
            views.MAN_Training, name='MAN_Training'),
    re_path(r'^MAN_trainingteam1/(?P<id>\d+)/$',
            views.MAN_trainingteam1, name='MAN_trainingteam1'),
    re_path(r'^MAN_traineestable/(?P<id>\d+)/$',
            views.MAN_traineestable, name='MAN_traineestable'),
    re_path(r'^MAN_trainingprofile/(?P<id>\d+)/$',
            views.MAN_trainingprofile, name='MAN_trainingprofile'),
    re_path(r'^MAN_completedtasktable/(?P<id>\d+)/$',
            views.MAN_completedtasktable, name='MAN_completedtasktable'),
    re_path(r'^MAN_topictable/(?P<id>\d+)/$',
            views.MAN_topictable, name='MAN_topictable'),



    # ************************  anwar   *********************************************

    re_path(r'^BRadmin_View_Trainers/(?P<id>\d+)/(?:(?P<did>\d+))?',
            views.BRadmin_View_Trainers, name='BRadmin_View_Trainers'),
    re_path(r'^BRadmin_View_Trainerprofile/(?P<id>\d+)/$',
            views.BRadmin_View_Trainerprofile, name='BRadmin_View_Trainerprofile'),

    re_path(r'^BRadmin_View_Currenttraineesoftrainer/(?P<id>\d+)/$',
            views.BRadmin_View_Currenttraineesoftrainer, name='BRadmin_View_Currenttraineesoftrainer'),

    re_path(r'^BRadmin_View_Previoustraineesoftrainer/(?P<id>\d+)/$',
            views.BRadmin_View_Previoustraineesoftrainer, name='BRadmin_View_Previoustraineesoftrainer'),

    re_path(r'^BRadmin_View_Currenttraineeprofile/(?P<id>\d+)/$',
            views.BRadmin_View_Currenttraineeprofile, name='BRadmin_View_Currenttraineeprofile'),

    re_path(r'^BRadmin_View_Currenttraineetasks/(?P<id>\d+)/$',
            views.BRadmin_View_Currenttraineetasks, name='BRadmin_View_Currenttraineetasks'),

    re_path(r'^BRadmin_View_Currenttraineeattendance/(?P<id>\d+)/$',
            views.BRadmin_View_Currenttraineeattendance, name='BRadmin_View_Currenttraineeattendance'),

    re_path(r'^BRadmin_View_Previoustraineesoftrainer/$',
            views.BRadmin_View_Previoustraineesoftrainer, name='BRadmin_View_Previoustraineesoftrainer'),

    re_path(r'^BRadmin_View_Previoustraineeprofile/(?P<id>\d+)/$',
            views.BRadmin_View_Previoustraineeprofile, name='BRadmin_View_Previoustraineeprofile'),

    re_path(r'^BRadmin_View_Previoustraineetasks/(?P<id>\d+)/$',
            views.BRadmin_View_Previoustraineetasks, name='BRadmin_View_Previoustraineetasks'),

    re_path(r'^BRadmin_View_Previoustraineeattendance/(?P<id>\d+)/$',
            views.BRadmin_View_Previoustraineeattendance, name='BRadmin_View_Previoustraineeattendance'),

    re_path(r'^BRadmin_View_Trainerattendance/(?P<id>\d+)/$',
            views.BRadmin_View_Trainerattendance, name='BRadmin_View_Trainerattendance'),

    re_path(r'^BRadmin_ViewTrainerattendancesort/(?P<id>\d+)/$',
            views.BRadmin_ViewTrainerattendancesort, name='BRadmin_ViewTrainerattendancesort'),

    re_path(r'^BRadmin_ViewCurrenttraineeattendancesort/(?P<id>\d+)/$',
            views.BRadmin_ViewCurrenttraineeattendancesort, name='BRadmin_ViewCurrenttraineeattendancesort'),

    re_path(r'^BRadmin_ViewPrevioustraineeattendancesort/(?P<id>\d+)/$',
            views.BRadmin_ViewPrevioustraineeattendancesort, name='BRadmin_ViewPrevioustraineeattendancesort'),

    re_path(r'^BRadmin_attendance/$', views.admin_page1, name='admin_page1'),
    re_path(r'^BRadmin_attendanceshow/$',
            views.admin_page3, name='admin_page3'),

    re_path(r'^admin_desi/$', views.admin_desi, name='admin_desi'),
    re_path(r'^admin_emp/$', views.admin_emp, name='admin_emp'),



    re_path(r'^MAN_View_Trainers/(?P<id>\d+)/(?:(?P<did>\d+))?',
            views.MAN_View_Trainers, name='MAN_View_Trainers'),
    re_path(r'^MAN_View_Trainerprofile/(?P<id>\d+)/$',
            views.MAN_View_Trainerprofile, name='MAN_View_Trainerprofile'),


    re_path(r'^MAN_View_Currenttraineesoftrainer/(?P<id>\d+)/$',
            views.MAN_View_Currenttraineesoftrainer, name='MAN_View_Currenttraineesoftrainer'),

    re_path(r'^MAN_View_Previoustraineesoftrainer/(?P<id>\d+)/$',
            views.MAN_View_Previoustraineesoftrainer, name='MAN_View_Previoustraineesoftrainer'),

    re_path(r'^MAN_View_Currenttraineeprofile/(?P<id>\d+)/$',
            views.MAN_View_Currenttraineeprofile, name='MAN_View_Currenttraineeprofile'),

    re_path(r'^MAN_View_Currenttraineetasks/(?P<id>\d+)/$',
            views.MAN_View_Currenttraineetasks, name='MAN_View_Currenttraineetasks'),

    re_path(r'^MAN_View_Currenttraineeattendance/(?P<id>\d+)/$',
            views.MAN_View_Currenttraineeattendance, name='MAN_View_Currenttraineeattendance'),

    re_path(r'^MAN_View_Previoustraineesoftrainer/$',
            views.MAN_View_Previoustraineesoftrainer, name='MAN_View_Previoustraineesoftrainer'),

    re_path(r'^MAN_View_Previoustraineeprofile/(?P<id>\d+)/$',
            views.MAN_View_Previoustraineeprofile, name='MAN_View_Previoustraineeprofile'),

    re_path(r'^MAN_View_Previoustraineetasks/(?P<id>\d+)/$',
            views.MAN_View_Previoustraineetasks, name='MAN_View_Previoustraineetasks'),

    re_path(r'^MAN_View_Previoustraineeattendance/(?P<id>\d+)/$',
            views.MAN_View_Previoustraineeattendance, name='MAN_View_Previoustraineeattendance'),

    re_path(r'^MAN_View_Trainerattendance/(?P<id>\d+)/$',
            views.MAN_View_Trainerattendance, name='MAN_View_Trainerattendance'),


    re_path(r'^MAN_ViewTrainerattendancesort/(?P<id>\d+)/$',
            views.MAN_ViewTrainerattendancesort, name='MAN_ViewTrainerattendancesort'),

    re_path(r'^MAN_ViewCurrenttraineeattendancesort/(?P<id>\d+)/$',
            views.MAN_ViewCurrenttraineeattendancesort, name='MAN_ViewCurrenttraineeattendancesort'),

    re_path(r'^MAN_ViewPrevioustraineeattendancesort/(?P<id>\d+)/$',
            views.MAN_ViewPrevioustraineeattendancesort, name='MAN_ViewPrevioustraineeattendancesort'),

    re_path(r'^MAN_dev_attendance/$', views.MAN_dev_attendance,
            name='MAN_dev_attendance'),

    re_path(r'^MAN_attendance/$', views.man_page1, name='man_page1'),
    re_path(r'^MAN_attendanceshow/$', views.man_page3, name='man_page3'),

    re_path(r'^man_desi/$', views.man_desi, name='man_desi'),
    re_path(r'^man_emp/$', views.man_emp, name='man_emp'),
    # ************************  anwar end  *********************************************



    # current projects-sharon -admin mod

    # re_path(r'^BRadmin_profiledash$', views.BRadmin_profiledash,name='BRadmin_profiledash'),
    re_path(r'^BRadmin_dept/$', views.BRadmin_dept, name='BRadmin_dept'),
    re_path(r'^BRadmin_pythons/$', views.BRadmin_pythons, name='BRadmin_pythons'),
    re_path(r'^BRadmin_projects/(?P<id>\d+)/$',
            views.BRadmin_projects, name='BRadmin_projects'),
    re_path(r'^BRadmin_proj_list/(?P<id>\d+)/$',
            views.BRadmin_proj_list, name='BRadmin_proj_list'),
    re_path(r'^BRadmin_proj_det/(?P<id>\d+)/$',
            views.BRadmin_proj_det, name='BRadmin_proj_det'),
    re_path(r'^BRadmin_proj_mngrs/(?P<id>\d+)/$',
            views.BRadmin_proj_mngrs, name='BRadmin_proj_mngrs'),
    re_path(r'^BRadmin_proj_mangrs1/(?P<id>\d+)/$',
            views.BRadmin_proj_mangrs1, name='BRadmin_proj_mangrs1'),
    re_path(r'^BRadmin_proj_mangrs2/(?P<id>\d+)/$',
            views.BRadmin_proj_mangrs2, name='BRadmin_proj_mangrs2'),
    re_path(r'^BRadmin_daily_report/(?P<id>\d+)/$',
            views.BRadmin_daily_report, name='BRadmin_daily_report'),
    re_path(r'^BRadmin_developers/(?P<id>\d+)/$',
            views.BRadmin_developers, name='BRadmin_developers'),


    # completed projects-subeeesh -admin mod

    re_path(r'^BRadmin_proj_cmpltd_new/(?P<id>\d+)/$',
            views.BRadmin_proj_cmpltd_new, name='BRadmin_proj_cmpltd_new'),
    re_path(r'^BRadmin_cmpltd_proj_det_new/(?P<id>\d+)/$',
            views.BRadmin_cmpltd_proj_det_new, name='BRadmin_cmpltd_proj_det_new'),
    re_path(r'^BRadmin_proj_mngrs_new/(?P<id>\d+)/$',
            views.BRadmin_proj_mngrs_new, name='BRadmin_proj_mngrs_new'),
    re_path(r'^BRadmin_proj_mangrs1_new/(?P<id>\d+)/$',
            views.BRadmin_proj_mangrs1_new, name='BRadmin_proj_mangrs1_new'),
    re_path(r'^BRadmin_proj_mangrs2_new/(?P<id>\d+)/$',
            views.BRadmin_proj_mangrs2_new, name='BRadmin_proj_mangrs2_new'),
    re_path(r'^BRadmin_developers_new/(?P<id>\d+)/$',
            views.BRadmin_developers_new, name='BRadmin_developers_new'),
    re_path(r'^BRadmin_daily_report_new/(?P<id>\d+)/$',
            views.BRadmin_daily_report_new, name='BRadmin_daily_report_new'),

    # current projects-sharon -admin mod

    # re_path(r'^MAN_profiledash$', views.MAN_profiledash,name='MAN_profiledash'),
    re_path(r'^MAN_dept$', views.MAN_dept, name='MAN_dept'),
    re_path(r'^MAN_pythons$', views.MAN_pythons, name='MAN_pythons'),
    re_path(r'^MAN_projects/(?P<id>\d+)/$',
            views.MAN_projects, name='MAN_projects'),
    re_path(r'^MAN_proj_list/(?P<id>\d+)/$',
            views.MAN_proj_list, name='MAN_proj_list'),
    re_path(r'^MAN_proj_det/(?P<id>\d+)/$',
            views.MAN_proj_det, name='MAN_proj_det'),
    re_path(r'^MAN_proj_mngrs/(?P<id>\d+)/$',
            views.MAN_proj_mngrs, name='MAN_proj_mngrs'),
    re_path(r'^MAN_proj_mangrs1/(?P<id>\d+)/$',
            views.MAN_proj_mangrs1, name='MAN_proj_mangrs1'),
    re_path(r'^MAN_proj_mangrs2/(?P<id>\d+)/$',
            views.MAN_proj_mangrs2, name='MAN_proj_mangrs2'),
    re_path(r'^MAN_daily_report/(?P<id>\d+)/$',
            views.MAN_daily_report, name='MAN_daily_report'),
    re_path(r'^MAN_developers/(?P<id>\d+)/$',
            views.MAN_developers, name='MAN_developers'),


    # completed projects-subeeesh -man mod

    re_path(r'^MAN_proj_cmpltd_new/(?P<id>\d+)/$',
            views.MAN_proj_cmpltd_new, name='MAN_proj_cmpltd_new'),
    re_path(r'^MAN_cmpltd_proj_det_new/(?P<id>\d+)/$',
            views.MAN_cmpltd_proj_det_new, name='MAN_cmpltd_proj_det_new'),
    re_path(r'^MAN_proj_mngrs_new/(?P<id>\d+)/$',
            views.MAN_proj_mngrs_new, name='MAN_proj_mngrs_new'),
    re_path(r'^MAN_proj_mangrs1_new/(?P<id>\d+)/$',
            views.MAN_proj_mangrs1_new, name='MAN_proj_mangrs1_new'),
    re_path(r'^MAN_proj_mangrs2_new/(?P<id>\d+)/$',
            views.MAN_proj_mangrs2_new, name='MAN_proj_mangrs2_new'),
    re_path(r'^MAN_developers_new/(?P<id>\d+)/$',
            views.MAN_developers_new, name='MAN_developers_new'),
    re_path(r'^MAN_daily_report_new/(?P<id>\d+)/$',
            views.MAN_daily_report_new, name='MAN_daily_report_new'),
    re_path(r'^MAN_training_department/$', views.MAN_training_department,name='MAN_training_department'),

    ########## end ##########

    # reported issue- akhil-admin mod

    re_path(r'^BRadmin_Reportedissue_department$',
            views.BRadmin_Reportedissue_department, name='BRadmin_Reportedissue_department'),
    re_path(r'^BRadmin_Reportedissue/(?P<id>\d+)/$',
            views.BRadmin_Reportedissue, name='BRadmin_Reportedissue'),
    re_path(r'^BRadmin_ReportedissueShow/(?P<id>\d+)/(?:(?P<did>\d+))/$',
            views.BRadmin_ReportedissueShow, name='BRadmin_ReportedissueShow'),
    re_path(r'^BRadmin_ReportedissueShow1/(?P<id>\d+)/$',
            views.BRadmin_ReportedissueShow1, name='BRadmin_ReportedissueShow1'),

    # reported issue- akhil-man mod

    re_path(r'^MAN_Reportedissue_department$',
            views.MAN_Reportedissue_department, name='MAN_Reportedissue_department'),
    re_path(r'^MAN_Reportedissue/(?P<id>\d+)/$',
            views.MAN_Reportedissue, name='MAN_Reportedissue'),
    re_path(r'^MAN_ReportedissueShow/(?P<id>\d+)/(?:(?P<did>\d+))?',
            views.MAN_ReportedissueShow, name='MAN_ReportedissueShow'),
    re_path(r'^MAN_ReportedissueShow1/(?P<id>\d+)/$',
            views.MAN_ReportedissueShow1, name='MAN_ReportedissueShow1'),
    re_path(r'^MAN_reported/(?P<id>\d+)/$',
            views.MAN_reported, name='MAN_reported'),

    ########## end ##########

    # task section-nimisha- man mod

    re_path(r'^MAN_tasks/$', views.MAN_tasks, name='MAN_tasks'),
    re_path(r'MAN_givetask/$', views.MAN_givetask, name='MAN_givetask'),
    re_path(r'^MAN_currenttasks/$', views.MAN_currenttasks,
            name='MAN_currenttasks'),
    re_path(r'^MAN_previoustasks/$', views.MAN_previoustasks,
            name='MAN_previoustasks'),
    re_path(r'MAN_taskemployee/$', views.MAN_taskemployee,
            name='MAN_taskemployee'),
    re_path(r'MAN_taskdesignation/$', views.MAN_taskdesignation,
            name='MAN_taskdesignation'),


    # task section-nimisha- admin mod

    re_path(r'^BRadmin_tasks/$', views.BRadmin_tasks, name='BRadmin_tasks'),
    re_path(r'BRadmin_givetask/$', views.BRadmin_givetask,
            name='BRadmin_givetask'),
    re_path(r'^BRadmin_currenttasks/$', views.BRadmin_currenttasks,
            name='BRadmin_currenttasks'),
    re_path(r'^BRadmin_previoustasks/$', views.BRadmin_previoustasks,
            name='BRadmin_previoustasks'),
    re_path(r'BRadmin_taskemployee/$', views.BRadmin_taskemployee,
            name='BRadmin_taskemployee'),
    re_path(r'BRadmin_taskdesignation/$', views.BRadmin_taskdesignation,
            name='BRadmin_taskdesignation'),
    re_path(r'^BRadmin_trainersdepartment$',
            views.BRadmin_trainersdepartment, name='BRadmin_trainersdepartment'),

    ########## end ##########


    # upcoming projects -safdhar -admin mod

    re_path(r'^BRadmin_upcoming/$', views.BRadmin_upcoming,
            name='BRadmin_upcoming'),
    re_path(r'^BRadmin_viewprojectform/$', views.BRadmin_viewprojectform,
            name='BRadmin_viewprojectform'),
    re_path(r'^BRadmin_acceptedprojects/$',
            views.BRadmin_acceptedprojects, name='BRadmin_acceptedprojects'),
    re_path(r'^BRadmin_rejected/$', views.BRadmin_rejected,
            name='BRadmin_rejected'),
    re_path(r'^BRadmin_createproject/$', views.BRadmin_createproject,
            name='BRadmin_createproject'),
    re_path(r'^BRadmin_upcomingpro/$', views.BRadmin_upcomingpro,
            name='BRadmin_upcomingpro'),
    re_path(r'^BRadmin_seradmintraineedesi1/$',
            views.BRadmin_seradmintraineedesi1, name='BRadmin_seradmintraineedesi1'),
    re_path(r'^BRadmin_seradmindesig/$', views.BRadmin_seradmindesig,
            name='BRadmin_seradmindesig'),
    re_path(r'^BRadmin_selectproject/$', views.BRadmin_selectproject,
            name='BRadmin_selectproject'),


    # upcoming projects -safdhar -man mod

    re_path(r'^MAN_upcoming/$', views.MAN_upcoming, name='MAN_upcoming'),
    re_path(r'^MAN_viewprojectform/$', views.MAN_viewprojectform,
            name='MAN_viewprojectform'),
    re_path(r'^MAN_acceptedprojects/$', views.MAN_acceptedprojects,
            name='MAN_acceptedprojects'),
    re_path(r'^MAN_rejected/$', views.MAN_rejected, name='MAN_rejected'),
    re_path(r'^MAN_upcomingprojectsview/$',
            views.MAN_upcomingprojectsview, name='MAN_upcomingprojectsview'),
    re_path(r'^MAN_createproject/$', views.MAN_createproject,
            name='MAN_createproject'),
    re_path(r'^MAN_seradmintraineedesi1/$',
            views.MAN_seradmintraineedesi1, name='MAN_seradmintraineedesi1'),
    re_path(r'^MAN_seradmindesig/$', views.MAN_seradmindesig,
            name='MAN_seradmindesig'),
    re_path(r'^Manager_selectproject/$', views.Manager_selectproject,
            name='Manager_selectproject'),


    # ********************meenu************************
    re_path(r'^man_newdept/$', views.man_newdept, name='man_newdept'),
    re_path(r'^man_dept/$', views.man_dept, name='man_dept'),
    re_path(r'^man_add_deptsave/$', views.man_add_deptsave,
            name='man_add_deptsave'),
    re_path(r'^man_delete/(?P<id>\d+)/$', views.man_delete, name='man_delete'),

    re_path(r'^newdept/$', views.newdept, name='newdept'),
    re_path(r'^add_dept/$', views.add_dept, name='add_dept'),
    re_path(r'^add_deptsave/$', views.add_deptsave, name='add_deptsave'),
    re_path(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),

    
    
    #***************************************christin**********************************

    re_path(r'^logout/$', views.logout,name='logout'),
    re_path(r'^internship/$', views.internshipform, name='internshipform'),
    re_path(r'^internship_save/$', views.internship_save,name='internship_save'),
    re_path(r'^leave1/$', views.leave1,name='leave1'),
    re_path(r'^registration/$', views.man_registration_form,name='man_registration_form'),
   
#     re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


    #Project manager
    #---------------------------------------------------------------------------------------------------------
    re_path(r'^pmanager_dash/', views.pmanager_dash,name="pmanager_dash"),
    re_path(r'^projectmanager_projects/', views.projectmanager_projects, name="projectmanager_projects"),
    re_path(r'^completepro/(?P<id>\d+)/$', views.completepro, name='completepro'),
    re_path(r'^pr_mg/$', views.pr_mg, name="pr_mg"),

    #nirmal
    re_path(r'^projectmanager_assignproject/', views.projectmanager_assignproject, name="projectmanager_assignproject"),

    #jensin
    re_path(r'^projectmanager_createproject/', views.projectmanager_createproject, name="projectmanager_createproject"),

    #maneesh
    re_path(r'^projectmanager_description/(?P<id>\d+)/', views.projectmanager_description, name="projectmanager_description"),
    re_path(r'^projectmanager_table', views.projectmanager_table, name="projectmanager_table"),
    re_path(r'^proMAN_acceptproj/(?P<id>\d+)/', views.proMAN_acceptproj, name="proMAN_acceptproj"),
    re_path(r'^proMAN_rejectproj/(?P<id>\d+)/', views.proMAN_rejectproj, name="proMAN_rejectproj"),
    re_path(r'^projectmanager_upprojects/', views.projectmanager_upprojects, name="projectmanager_upprojects"),

    #praveesh
    re_path(r'^projectmanager_accepted_projects/', views.projectmanager_accepted_projects, name="projectmanager_accepted_projects"),
    re_path(r'^projectmanager_rejected_projects/', views.projectmanager_rejected_projects, name="projectmanager_rejected_projects"),
    re_path(r'^projectmanager_edit_assigned_projects/', views.projectmanager_edit_assigned_projects, name="projectmanager_edit_assigned_projects"),
    re_path(r'^projectManager_edit_projects_status/', views.projectManager_edit_projects_status, name="projectManager_edit_projects_status"),



    #amal#bibin#rohit#abin
    re_path(r'^manindex/$', views.manindex, name='manindex'),
    re_path(r'^projectmanEmp/$', views.projectmanEmp, name='projectmanEmp'),
    re_path(r'^projectmanDev/$', views.projectmanDev, name='projectmanDev'),
    re_path(r'^projectman_trainees/$', views.projectman_trainees, name='projectman_trainees'),
    re_path(r'^projectmanDevDashboard/(?P<id>\d+)/$', views.projectmanDevDashboard, name='projectmanDevDashboard'),
    re_path(r'^projectman_developer_attendance/(?P<id>\d+)/$', views.projectman_developer_attendance, name='projectman_developer_attendance'),

    re_path(r'^projectman_team/(?P<id>\d+)/$', views.projectman_team, name='projectman_team'),
    re_path(r'^projectman_team_profile/(?P<id>\d+)/$', views.projectman_team_profile, name='projectman_team_profile'),
    re_path(r'^projectman_team_attendance/(?P<id>\d+)/$', views.projectman_team_attendance, name='projectman_team_attendance'),
    re_path(r'^projectman_team_attandance/(?P<id>\d+)/$', views.projectman_team_attandance, name='projectman_team_attandance'),

    re_path(r'^projectMANattendance/$', views.projectMANattendance, name='projectMANattendance'),
    re_path(r'^projectMANattandance/$', views.projectMANattandance, name='projectMANattandance'),

    re_path(r'^projectMANreportedissues$', views.projectMANreportedissues, name='projectMANreportedissues'),
    re_path(r'^projectMANreportedissue$', views.projectMANreportedissue, name='projectMANreportedissue'),
    re_path(r'^projectMANreportissue$', views.projectMANreportissue, name='projectMANreportissue'),
    re_path(r'^projectmanagerreportedissue2/(?P<id>\d+)/$', views.projectmanagerreportedissue2, name='projectmanagerreportedissue2'),
    re_path(r'^projectmanagerreportedissue3/(?P<id>\d+)/$', views.projectmanagerreportedissue3, name='projectmanagerreportedissue3'),
    re_path(r'^MANreportsuccess$', views.MANreportsuccess, name='MANreportsuccess'),
    re_path(r'^projectreply/(?P<id>\d+)/$', views.projectreply, name='projectreply'), 
    

    re_path(r'^projectMANleave/$', views.projectMANleave, name='projectMANleave'),
    re_path(r'^projectMANleavereq/$', views.projectMANleavereq, name='projectMANleavereq'),
    re_path(r'^projectMANreqedleave/$', views.projectMANreqedleave, name='projectMANreqedleave'),

    re_path(r'^Manager_employees/$', views.Manager_employees, name='Manager_employees'),
    re_path(r'^projectManager_tl/$', views.projectManager_tl, name='projectManager_tl'),
    re_path(r'^projectManager_tl_dashboard/(?P<id>\d+)/$', views.projectManager_tl_dashboard, name='projectManager_tl_dashboard'),
    re_path(r'^man_tl_attendance/$', views.man_tl_attendance, name='man_tl_attendance'), 

    re_path(r'^projectmanager_currentproject/$', views.projectmanager_currentproject, name='projectmanager_currentproject'), 
    re_path(r'^projectmanager_currentdetail/(?P<id>\d+)/$', views.projectmanager_currentdetail, name='projectmanager_currentdetail'), 
    
    re_path(r'^projectmanager_completeproject/$', views.projectmanager_completeproject, name='projectmanager_completeproject'),
    re_path(r'^projectmanager_completedetail/(?P<id>\d+)/$', views.projectmanager_completedetail, name='projectmanager_completedetail'), 
    re_path(r'^projectmanager_completeteam/(?P<id>\d+)/$', views.projectmanager_completeteam, name='projectmanager_completeteam'),
    re_path(r'^projectmanager_teaminvolved/(?P<id>\d+)/$', views.projectmanager_teaminvolved, name='projectmanager_teaminvolved'),
    re_path(r'^projectmanager_devteam/(?P<id>\d+)/$', views.projectmanager_devteam, name='projectmanager_devteam'),

    re_path(r'^projectmanager_currentteam/(?P<id>\d+)/$', views.projectmanager_currentteam, name='projectmanager_currentteam'),
    re_path(r'^projectmanager_currenttl/(?P<id>\d+)/$', views.projectmanager_currenttl, name='projectmanager_currenttl'),
    re_path(r'^projectmanager_completetl/(?P<id>\d+)/$', views.projectmanager_completetl, name='projectmanager_completetl'),
    re_path(r'^projectmanager_tlreported/$', views.projectmanager_tlreported, name='projectmanager_tlreported'), 
    re_path(r'^TLlogout/$', views.TLlogout, name='TLlogout'),
    re_path(r'^ProMANlogout/$', views.ProMANlogout, name='ProMANlogout'),
 

    re_path(r'^projectmanager_accepted_projects', views.projectmanager_accepted_projects, name="projectmanager_accepted_projects"),    
    re_path(r'^projectmanager_rejected_projects', views.projectmanager_rejected_projects, name="projectmanager_rejected_projects"),


    re_path(r'^projectmanager_completeproject$', views.projectmanager_completeproject, name='projectmanager_completeproject'),
    re_path(r'^projectmanager_completedetail/(?P<id>\d+)/$', views.projectmanager_completedetail, name='projectmanager_completedetail'), 
    re_path(r'^projectmanager_completeteam/(?P<id>\d+)/$', views.projectmanager_completeteam, name='projectmanager_completeteam'),
    re_path(r'^currentperformance/(?P<id>\d+)/$', views.currentperformance, name='currentperformance'),
    re_path(r'^projectmanager_completetl$', views.projectmanager_completetl, name='projectmanager_completetl'),

    re_path(r'^projectmanager_assignproject/', views.projectmanager_assignproject, name="projectmanager_assignproject"),

    re_path(r'^projectmanager_createproject', views.projectmanager_createproject, name="projectmanager_createproject"),
    re_path(r'^pro_allocatetl/', views.pro_allocatetl, name="pro_allocatetl"),
    re_path(r'^projectmanager_projectlist/', views.projectmanager_projectlist, name="projectmanager_projectlist"),
    re_path(r'^projectmanager_projectstatus/(?P<id>\d+)/', views.projectmanager_projectstatus, name="projectmanager_projectstatus"),

#---------------------------------------------------------------------------------------------------------------------------

#  Teamleader
    re_path(r'^projectreplytl/(?P<id>\d+)/$', views.projectreplytl, name='projectreplytl'), 
    re_path(r'^TLdashboard/$', views.TLdashboard, name='TLdashboard'),
    re_path(r'^TLattendance/$', views.TLattendance, name='TLattendance'),
    re_path(r'^TLattendancesort/$', views.TLattendancesort, name='TLattendancesort'),
    re_path(r'^TLprojects/$', views.TLprojects, name='TLprojects'),
    re_path(r'^TLreportissues/$', views.TLreportissues, name='TLreportissues'),
    re_path(r'^TLtasks/$', views.TLtasks, name='TLtasks'),
    re_path(r'^TLleave/$', views.TLleave, name='TLleave'),
    re_path(r'^tlprojecttasks/(?P<id>\d+)/$', views.tlprojecttasks, name='tlprojecttasks'),
    re_path(r'^TLreportedissue1/$', views.TLreportedissue1, name='TLreportedissue1'),
    re_path(r'^TLreportedissue2/(?P<id>\d+)/$', views.TLreportedissue2, name='TLreportedissue2'),
    re_path(r'^TLreport1/$', views.TLreport1, name='TLreport1'),
    re_path(r'^tlgivetask/$', views.tlgivetask, name='tlgivetask'),
    re_path(r'^TLreportsuccess/$', views.TLreportsuccess, name='TLreportsuccess'),
    re_path(r'^tltaskstatus/(?P<id>\d+)/$', views.tltaskstatus, name='tltaskstatus'),
    re_path(r'^tlsplittask/(?P<id>\d+)/$', views.tlsplittask, name='tlsplittask'), 
    re_path(r'^TLgavetask/(?P<id>\d+)/$', views.TLgavetask, name='TLgavetask'),
    re_path(r'^TLgivetasks/(?P<id>\d+)/$', views.TLgivetasks, name='TLgivetasks'),
    re_path(r'^TLtaskformsubmit/(?P<id>\d+)/$', views.TLtaskformsubmit, name='TLtaskformsubmit'),
    re_path(r'^TLleavereq/$', views.TLleavereq, name='TLleavereq'),
    re_path(r'^TLreqedleave/$', views.TLreqedleave, name='TLreqedleave'),
    re_path(r'^tl_leave_form/$', views.tl_leave_form, name='tl_leave_form'),
    re_path(r'^extensionsave/(?P<id>\d+)/$', views.extensionsave, name='extensionsave'),
    re_path(r'^extensionapprove/(?P<id>\d+)/$', views.extensionapprove, name='extensionapprove'),
    re_path(r'^extensionreject/(?P<id>\d+)/$', views.extensionreject, name='extensionreject'),
    re_path(r'^tlprojectsave/(?P<id>\d+)/$', views.tlprojectsave, name='tlprojectsave'),
    re_path(r'^pdetailsave/(?P<id>\d+)/$', views.pdetailsave, name='pdetailsave'),
    re_path(r'^devtlreported/$', views.devtlreported, name='devtlreported'),
    re_path(r'^tldevview/(?P<id>\d+)/$', views.tldevview, name='tldevview'),
    re_path(r'^TLtasksub/(?P<id>\d+)/$', views.TLtasksub, name='TLtasksub'),
    re_path(r'^devtasksub/(?P<id>\d+)/$', views.devtasksub, name='devtasksub'),
    re_path(r'^testasksub/(?P<id>\d+)/$', views.testasksub, name='testasksub'),
    # re_path(r'^TLleave$', views.TLleave, name='TLleave'),

    # re_path(r'^TLleavereq$', views.TLleavereq, name='TLleavereq'), 
    # re_path(r'^TLreqedleave$', views.TLreqedleave, name='TLreqedleave'),

#-------------------------------------------------------------------------------------------------------
#tester module

    re_path(r'^TSassigned/(?P<id>\d+)/$', views.TSassigned, name='TSassigned'),
    re_path(r'^TSdashboard/$', views.TSdashboard, name='TSdashboard'),
    re_path(r'^TSpayment/$', views.TSpayment, name='TSpayment'),    
    re_path(r'^TSproject/$', views.TSproject, name='TSproject'),
    re_path(r'^TSprojectdetails/(?P<pid>\d+)/$', views.TSprojectdetails, name='TSprojectdetails'),
    re_path(r'^TSsubmitted/(?P<id>\d+)/$', views.TSsubmitted, name='TSsubmitted'),
     re_path(r'^TSsubmittedsave/(?P<id>\d+)/$', views.TSsubmittedsave, name='TSsubmittedsave'),
    re_path(r'^TStask/$', views.TStask, name='TStask'),
    re_path(r'^TSsucess/$', views.TSsucess, name='TSsucess'),

    re_path(r'^testersave/(?P<uid>\d+)/(?P<pid>\d+)/$', views.testersave, name='testersave'),
    re_path(r'^projectdetailsave/(?P<uid>\d+)/(?P<pid>\d+)/$', views.projectdetailsave, name='projectdetailsave'),

#-------------------------------------------------------------------------------------------------------------------------------
#developer module
    re_path(r'^devindex/$', views.devindex, name='devindex'),
    re_path(r'^devdashboard/$', views.devdashboard, name='devdashboard'),
    re_path(r'^devReportedissues/$', views.devReportedissues, name='devReportedissues'),
    re_path(r'^devreportissue/$', views.devreportissue, name='devreportissue'),
    re_path(r'^devreportedissue/$', views.devreportedissue, name='devreportedissue'),
    re_path(r'^devsuccess/$', views.devsuccess, name='devsuccess'),
    re_path(r'^devissues/(?P<id>\d+)/$', views.devissues, name='devissues'),
    re_path(r'^dev_leave_form/$', views.dev_leave_form, name='dev_leave_form'),
    re_path(r'^dev_task_submit/$', views.dev_task_submit, name='dev_task_submit'),
    re_path(r'^DEVtaskformsubmit/(?P<id>\d+)/$', views.DEVtaskformsubmit, name='DEVtaskformsubmit'),
    re_path(r'^DEVtasksumitted/$', views.DEVtasksumitted, name='DEVtasksumitted'),
    re_path(r'^DEVtaskstatus/(?P<id>\d+)/$', views.DEVtaskstatus, name='DEVtaskstatus'),
    re_path(r'^DEVextension/(?P<id>\d+)/$', views.DEVextension, name='DEVextension'),
    re_path(r'^devprjsave/(?P<id>\d+)/$', views.devprjsave, name='devprjsave'),
    


    re_path(r'^Devapplyleav/$', views.Devapplyleav, name='Devapplyleav'),
    re_path(r'^Devapplyleav1/$', views.Devapplyleav1, name='Devapplyleav1'),
    re_path(r'^Devapplyleav2/$', views.Devapplyleav2, name='Devapplyleav2'),
    re_path(r'^Devleaverequiest/$', views.Devleaverequiest, name='Devleaverequiest'),
    re_path(r'^Devattendance/$', views.Devattendance, name='Devattendance'),
    re_path(r'^Devattendancesort/$', views.Devattendancesort, name='Devattendancesort'),
    re_path(r'^Devapplyleav3/$', views.Devapplyleav3, name='Devapplyleav3'),



    re_path(r'^DEVprojects/$', views.DEVprojects, name='DEVprojects'),
    re_path(r'^DEVsuccess/$', views.DEVsuccess, name='DEVsuccess'),
    re_path(r'^DEVtable/(?P<id>\d+)/$', views.DEVtable, name='DEVtable'),
    re_path(r'^DEVtask/(?P<id>\d+)/$', views.DEVtask, name='DEVtask'),
    re_path(r'^DEVtaskform/(?P<id>\d+)/$', views.DEVtaskform, name='DEVtaskform'),
    re_path(r'^DEVtaskmain/$', views.DEVtaskmain, name='DEVtaskmain'),
    re_path(r'^devlogout/$', views.devlogout, name='devlogout'),
    
    
    
    #***********************internship**************************
   
    re_path(r'^man_internship_view/$', views.man_internship_view, name="man_internship_view"),
    re_path(r'^BRadmin_internship_view/$', views.BRadmin_internship_view, name="BRadmin_internship_view"),
    re_path(r'^registrationview/$', views.registrationview, name="registrationview"),
    re_path(r'^registrationviewman/$', views.registrationviewman, name="registrationviewman"),
    re_path(r'^man_internship/$', views.man_internship, name="man_internship"),
    re_path(r'^BRadmin_internship/$', views.BRadmin_internship, name="BRadmin_internship"),
    re_path(r'^man_internship_date$', views.man_internship_date, name="man_internship_date"),
    re_path(r'^man_internship_dateview$', views.man_internship_dateview, name="man_internship_dateview"),
    re_path(r'^BRadmin_internship_date$', views.BRadmin_internship_date, name="BRadmin_internship_date"),
    re_path(r'^BRadmin_internship_dateview$', views.BRadmin_internship_dateview, name="BRadmin_internship_dateview"),
    
    
    re_path(r'^BRadmin_internship_update/(?P<id>\d+)/$', views.BRadmin_internship_update, name="BRadmin_internship_update"),
    re_path(r'^internshipupdatesave/(?P<id>\d+)/$', views.internshipupdatesave, name="internshipupdatesave"),
    re_path(r'^interndelete/(?P<id>\d+)/$', views.interndelete, name="interndelete"),  
    re_path(r'^maninterndelete/(?P<id>\d+)/$', views.maninterndelete, name="maninterndelete"),  
    re_path( r'^pdf/(?P<id>\d+)/', views.render_pdf_view, name='pdf'),
    re_path( r'^certificate_intrn/(?P<id>\d+)/', views.certificate_intrn, name='certificate_intrn'),
    
    #***********************registration***********************
    re_path(r'^man_registration/$', views.man_registration, name="man_registration"),
    re_path(r'^BRadmin_registration/$', views.BRadmin_registration, name="BRadmin_registration"),
    re_path(r'^BRadmin_resign/$', views.BRadmin_resign, name="BRadmin_resign"),
    re_path(r'^man_resign/$', views.man_resign, name="man_resign"),
    re_path(r'^man_registration_update/(?P<id>\d+)/$', views.man_registration_update, name="man_registration_update"),
    re_path(r'^registrationupdatesave/(?P<id>\d+)/$', views.registrationupdatesave, name="registrationupdatesave"),
    re_path(r'^registrationdelete/(?P<id>\d+)/$', views.registrationdelete, name="registrationdelete"),
    
    #########################  trainee Payment New ######################
    re_path(r'^trainee_payment$', views.trainee_payment,name='trainee_payment'),
    re_path(r'^trainee_payment_addpayment$', views.trainee_payment_addpayment,name='trainee_payment_addpayment'),
    re_path(r'^trainee_payment_viewpayment$', views.trainee_payment_viewpayment,name='trainee_payment_viewpayment'),
#################################Accounts module########################

    # re_path(r'^accounts_Dashboard/$', views.accounts_Dashboard, name='accounts_Dashboard'),
    # re_path(r'^account_accounts/$', views.account_accounts,name='account_accounts'),
    # re_path(r'^imagechange_accounts/$', views.imagechange_accounts, name='imagechange_accounts'),
    # re_path(r'^changepassword_accounts/$', views.changepassword_accounts,name='changepassword_accounts'),
    # re_path(r'^accounts_employee/$', views.accounts_employee, name='accounts_employee'),
    # re_path(r'^accounts_emp_dep/(?P<id>\d+)/$', views.accounts_emp_dep, name='accounts_emp_dep'),
    # re_path(r'^accounts_emp_list/(?P<id>\d+)(?:/(?P<pk>\d+))?', views.accounts_emp_list, name='accounts_emp_list'),
    # re_path(r'^accounts_emp_details/(?P<id>\d+)/$', views.accounts_emp_details, name='accounts_emp_details'),
    # re_path(r'^accounts_payment/$', views.accounts_payment, name='accounts_payment'),
    # re_path(r'^accounts_payment_dep/(?P<id>\d+)/$', views.accounts_payment_dep, name='accounts_payment_dep'),
    # re_path(r'^accounts_payment_list/(?P<id>\d+)(?:/(?P<pk>\d+))?', views.accounts_payment_list, name='accounts_payment_list'),
    # re_path(r'^accounts_coursefee/$',views.accounts_coursefee,name="accounts_coursefee"),
    # re_path(r'^accounts_coursefee_addnew$',views.accounts_coursefee_addnew,name="accounts_coursefee_addnew"),
    # re_path(r'^coursefeeupdate/(?P<id>\d+)/$',views.coursefeeupdate,name="coursefeeupdate"),
    # re_path(r'^coursedelete/(?P<id>\d+)$',views.coursedelete,name="coursedelete"),
    # re_path(r'^accounts_registration_details/$', views.accounts_registration_details, name='accounts_registration_details'),
    # re_path(r'^reminder/(?P<id>\d+)$',views.reminder,name="reminder"), 
    # re_path(r'^verify/(?P<id>\d+)$',views.verify,name="verify"), 
    # re_path(r'^accounts_payment_detail_list/(?P<id>\d+)$',views.accounts_payment_detail_list,name="accounts_payment_detail_list"),
    # re_path(r'^accounts_expenses/$', views.accounts_expenses, name='accounts_expenses'),
    # re_path(r'^accounts_expenses_viewEdit/(?P<id>\d+)$', views.accounts_expenses_viewEdit, name='accounts_expenses_viewEdit'),
    # re_path(r'^accounts_expenses_viewEdit_Update/(?P<id>\d+)$', views.accounts_expenses_viewEdit_Update, name='accounts_expenses_viewEdit_Update'),
    # re_path(r'^accounts_expense_newTransaction/$', views.accounts_expense_newTransaction, name='accounts_expense_newTransaction'),
    # re_path(r'^account_report/$',views.account_report,name="account_report"),
    # re_path(r'^account_report_issue/$',views.account_reportt_issue,name="account_reportt_issue"),
    # re_path(r'^account_reported_issue/$',views.account_reported_issue,name="account_reported_issue"),
    # re_path(r'^account_payment_details/(?P<id>\d+)/$', views.account_payment_details, name='account_payment_details'),
    # re_path(r'^account_payment_salary/(?P<id>\d+)/$', views.account_payment_salary, name='account_payment_salary'),
    # re_path(r'^account_payment_view/(?P<id>\d+)/$', views.account_payment_view, name='account_payment_view'),
    # re_path(r'^accounts_payslip$', views.accounts_payslip, name='accounts_payslip'),
    # re_path(r'^accounts_acntpay$', views.accounts_acntpay, name='accounts_acntpay'),
    # re_path(r'^accounts_paydetails/(?P<id>\d+)/(?P<tid>\d+)/$', views.accounts_paydetails, name='accounts_paydetails'),
    # re_path(r'^accounts_print/(?P<id>\d+)/(?P<tid>\d+)/$', views.accounts_print,name='accounts_print'),
    # re_path(r'^accounts_add_bank_acnt/(?P<id>\d+)/$', views.accounts_add_bank_acnt, name='accounts_add_bank_acnt'),
    # re_path(r'^accounts_bank_acnt_details/(?P<id>\d+)/$', views.accounts_bank_acnt_details, name='accounts_bank_acnt_details'),
    # re_path(r'^accounts_salary_details/(?P<id>\d+)/$', views.accounts_salary_details, name='accounts_salary_details'),
    # re_path(r'^logout5/$', views.logout5, name='logout5'),

    re_path(r'^accounts_Dashboard/$', views.accounts_Dashboard, name='accounts_Dashboard'),
    re_path(r'^account_accounts/$', views.account_accounts,name='account_accounts'),
    re_path(r'^imagechange_accounts/$', views.imagechange_accounts, name='imagechange_accounts'),
    re_path(r'^changepassword_accounts/$', views.changepassword_accounts,name='changepassword_accounts'),
    re_path(r'^accounts_employee/$', views.accounts_employee, name='accounts_employee'),
    re_path(r'^accounts_emp_dep/(?P<id>\d+)/$', views.accounts_emp_dep, name='accounts_emp_dep'),
    re_path(r'^accounts_emp_list/(?P<id>\d+)(?:/(?P<pk>\d+))?', views.accounts_emp_list, name='accounts_emp_list'),
    re_path(r'^accounts_emp_details/(?P<id>\d+)/$', views.accounts_emp_details, name='accounts_emp_details'),
    re_path(r'^accounts_payment/$', views.accounts_payment, name='accounts_payment'),
    re_path(r'^accounts_payment_dep/(?P<id>\d+)/$', views.accounts_payment_dep, name='accounts_payment_dep'),
    re_path(r'^accounts_payment_list/(?P<id>\d+)(?:/(?P<pk>\d+))?', views.accounts_payment_list, name='accounts_payment_list'),
    re_path(r'^accounts_coursefee/$',views.accounts_coursefee,name="accounts_coursefee"),
    re_path(r'^accounts_coursefee_addnew$',views.accounts_coursefee_addnew,name="accounts_coursefee_addnew"),
    re_path(r'^coursefeeupdate/(?P<id>\d+)/$',views.coursefeeupdate,name="coursefeeupdate"),
    re_path(r'^coursedelete/(?P<id>\d+)$',views.coursedelete,name="coursedelete"),
    re_path(r'^accounts_registration_details/$', views.accounts_registration_details, name='accounts_registration_details'),
    re_path(r'^reminder/(?P<id>\d+)$',views.reminder,name="reminder"), 
    re_path(r'^verify/(?P<id>\d+)$',views.verify,name="verify"), 
    re_path(r'^accounts_payment_detail_list/(?P<id>\d+)$',views.accounts_payment_detail_list,name="accounts_payment_detail_list"),
    re_path(r'^accounts_expenses/$', views.accounts_expenses, name='accounts_expenses'),
    re_path(r'^accounts_expenses_viewEdit/(?P<id>\d+)$', views.accounts_expenses_viewEdit, name='accounts_expenses_viewEdit'),
    re_path(r'^accounts_expenses_viewEdit_Update/(?P<id>\d+)$', views.accounts_expenses_viewEdit_Update, name='accounts_expenses_viewEdit_Update'),
    re_path(r'^accounts_expense_newTransaction/$', views.accounts_expense_newTransaction, name='accounts_expense_newTransaction'),
    re_path(r'^account_report/$',views.account_report,name="account_report"),
    re_path(r'^account_report_issue/$',views.account_reportt_issue,name="account_reportt_issue"),
    re_path(r'^account_reported_issue/$',views.account_reported_issue,name="account_reported_issue"),
    re_path(r'^account_payment_details/(?P<id>\d+)/$', views.account_payment_details, name='account_payment_details'),
    re_path(r'^account_payment_salary/(?P<id>\d+)/$', views.account_payment_salary, name='account_payment_salary'),
    re_path(r'^account_payment_view/(?P<id>\d+)/$', views.account_payment_view, name='account_payment_view'),
    re_path(r'^accounts_payslip$', views.accounts_payslip, name='accounts_payslip'),
    re_path(r'^accounts_acntpay$', views.accounts_acntpay, name='accounts_acntpay'),
    re_path(r'^accounts_paydetails/(?P<id>\d+)/(?P<tid>\d+)/$', views.accounts_paydetails, name='accounts_paydetails'),
    re_path(r'^accounts_print/(?P<id>\d+)/(?P<tid>\d+)/$', views.accounts_print,name='accounts_print'),
    re_path(r'^accounts_add_bank_acnt/(?P<id>\d+)/$', views.accounts_add_bank_acnt, name='accounts_add_bank_acnt'),
    re_path(r'^accounts_bank_acnt_details/(?P<id>\d+)/$', views.accounts_bank_acnt_details, name='accounts_bank_acnt_details'),
    re_path(r'^accounts_salary_details/(?P<id>\d+)/$', views.accounts_salary_details, name='accounts_salary_details'),
    re_path(r'^logout5/$', views.logout5, name='logout5'),
    
    # ----
    
    
    # re_path(r'^accounts_leavehistory$',views.accounts_leavehistory, name="accounts_leavehistory"),
    # re_path(r'^accounts_leavehistory_department/(?P<id>\d+)/$',views.accounts_leavehistory_department, name="accounts_leavehistory_department"),
    # re_path(r'^accounts_leavehistory_employees/(?P<id>\d+)/(?P<id1>\d+)/$',views.accounts_leavehistory_employees, name="accounts_leavehistory_employees"),
    # re_path(r'^accounts_emp_leavehistory/(?P<id>\d+)/$',views.accounts_emp_leavehistory, name="accounts_emp_leavehistory"),
    
    re_path(r'^accounts_leavehistory$',views.accounts_leavehistory, name="accounts_leavehistory"),
    re_path(r'^accounts_leavehistory_department/(?P<id>\d+)/$',views.accounts_leavehistory_department, name="accounts_leavehistory_department"),
    re_path(r'^accounts_leavehistory_employees/(?P<id>\d+)/(?P<id1>\d+)/$',views.accounts_leavehistory_employees, name="accounts_leavehistory_employees"),
    re_path(r'^accounts_emp_leavehistory/(?P<id>\d+)/$',views.accounts_emp_leavehistory, name="accounts_emp_leavehistory"),    
    
    
    re_path(r'^offerletter/(?P<id>\d+)/$', views.offerletter, name="offerletter"),
    re_path(r'^relieveletter/(?P<id>\d+)/$', views.relieveletter, name="relieveletter"),
    re_path(r'^experienceletter/(?P<id>\d+)/$', views.experienceletter, name="experienceletter"),
   
    # re_path(r'^accounts_internship/', views.accounts_internship, name="accounts_internship"),
    # re_path(r'^accounts_internship_payment_pending/', views.accounts_internship_payment_pending, name="accounts_internship_payment_pending"),
    # re_path(r'^addamount/(?P<id>\d+)/', views.addamount, name="addamount"),
    # re_path(r'^accounts_internship_type_sel/(?P<id>\d+)/', views.accounts_internship_type_sel, name="accounts_internship_type_sel"),
    # re_path(r'^accounts_internship_verify/(?P<id>\d+)/', views.accounts_internship_verify, name="accounts_internship_verify"),
    # re_path(r'^accounts_internship_complete/(?P<id>\d+)/', views.accounts_internship_complete, name="accounts_internship_complete"),

    # re_path(r'^accounts_internship_viewall/', views.accounts_internship_viewall, name="accounts_internship_viewall"),
    
re_path(r'^accounts_internship/', views.accounts_internship, name="accounts_internship"),
    re_path(r'^accounts_internship_payment_pending/', views.accounts_internship_payment_pending, name="accounts_internship_payment_pending"),
    re_path(r'^addamount/(?P<id>\d+)/', views.addamount, name="addamount"),
    re_path(r'^accounts_internship_type_sel/(?P<id>\d+)/', views.accounts_internship_type_sel, name="accounts_internship_type_sel"),
    re_path(r'^accounts_internship_verify/(?P<id>\d+)/', views.accounts_internship_verify, name="accounts_internship_verify"),
    re_path(r'^accounts_internship_complete/(?P<id>\d+)/', views.accounts_internship_complete, name="accounts_internship_complete"),

    re_path(r'^accounts_internship_viewall/', views.accounts_internship_viewall, name="accounts_internship_viewall"),
    


#######################    jishnu   #############################

    # re_path(r'^accounts_intrenship_type/$',views.accounts_intrenship_type, name="accounts_intrenship_type"),
    # re_path(r'^accounts_intrenship_add/$',views.accounts_intrenship_add, name="accounts_intrenship_add"),
    
    re_path(r'^accounts_intrenship_type/$',views.accounts_intrenship_type, name="accounts_intrenship_type"),
    re_path(r'^accounts_intrenship_add/$',views.accounts_intrenship_add, name="accounts_intrenship_add"),
    
    re_path(r'^internshiptypeupdate/(?P<id>\d+)/$',views.internshiptypeupdate,name="internshiptypeupdate"),
    re_path(r'^internshiptypedelete/(?P<id>\d+)/$',views.internshiptypedelete,name="internshiptypedelete"),
    re_path(r'^trainer_currentprogress/(?P<id>\d+)$',views.trainer_currentprogress, name='trainer_currentprogress'),
    re_path(r'^BRadmin_new_registration/$', views.BRadmin_new_registration, name="BRadmin_new_registration"),
    re_path(r'^BRadmin_internship_pending/$', views.BRadmin_internship_pending, name="BRadmin_internship_pending"),
    re_path(r'^BRadmin_internship_acc_approved/$', views.BRadmin_internship_acc_approved, name="BRadmin_internship_acc_approved"),
    re_path(r'^registrationstatus/(?P<id>\d+)/$', views.registrationstatus, name="registrationstatus"),
    re_path(r'^BRadmin_accounts/$', views.BRadmin_accounts, name='BRadmin_accounts'),
    re_path(r'^BRadmin_accounts_traineepayment_notverified/$', views.BRadmin_accounts_traineepayment_notverified, name='BRadmin_accounts_traineepayment_notverified'),
    re_path(r'^BRadmin_accounts_traineepayment_pending/$', views.BRadmin_accounts_traineepayment_pending, name='BRadmin_accounts_traineepayment_pending'),
    re_path(r'^BRadmin_accounts_newtrainees/$', views.BRadmin_accounts_newtrainees, name='BRadmin_accounts_newtrainees'),
    re_path(r'^BRadmin_accounts_salaried_employees/$', views.BRadmin_accounts_salaried_employees, name='BRadmin_accounts_salaried_employees'),
    re_path(r'^BRadmin_accounts_salary_employees/$', views.BRadmin_accounts_salary_employees, name='BRadmin_accounts_salary_employees'),
    re_path(r'^BRadmin_accounts_internship/$', views.BRadmin_accounts_internship, name='BRadmin_accounts_internship'),
    re_path(r'^BRadmin_accounts_internship_viewall/$', views.BRadmin_accounts_internship_viewall, name='BRadmin_accounts_internship_viewall'),
    re_path(r'^BRadmin_accounts_internship_payment_pending/$', views.BRadmin_accounts_internship_payment_pending, name='BRadmin_accounts_internship_payment_pending'),
    re_path(r'^BRadmin_accounts_internship_viewbydate/$', views.BRadmin_accounts_intrenship_viewbydate, name="BRadmin_accounts_internship_viewbydate"),
    re_path(r'^BRadmin_accounts_internship_dateview$', views.BRadmin_accounts_internship_dateview, name="BRadmin_accounts_internship_dateview"),
    # re_path(r'^accounts_internship_dateview$', views.accounts_internship_dateview, name="accounts_internship_dateview"),
    
    re_path(r'^accounts_internship_dateview$', views.accounts_internship_dateview, name="accounts_internship_dateview"),

    re_path(r'^BRadmin_accounts_internship_update/(?P<id>\d+)/$', views.BRadmin_accounts_internship_update, name="BRadmin_accounts_internship_update"),
    re_path(r'^BRadmin_accounts_interndelete/(?P<id>\d+)/$', views.BRadmin_accounts_interndelete, name="BRadmin_accounts_interndelete"),
    re_path(r'^BRadmin_accounts_internshipupdatesave/(?P<id>\d+)/$', views.BRadmin_accounts_internshipupdatesave, name="BRadmin_accounts_internshipupdatesave"),
    re_path(r'^BRadmin_monthdays/$',views.BRadmin_monthdays, name='BRadmin_monthdays'),
    re_path(r'^BRadmin_viewdays/$',views.BRadmin_viewdays, name='BRadmin_viewdays'),
    re_path(r'^BRadmin_salary_given/$',views.BRadmin_salary_given, name='BRadmin_salary_given'),
    re_path(r'^BRadmin_salary_pending/$',views.BRadmin_salary_pending, name='BRadmin_salary_pending'),
    re_path(r'^BRadmin_project_dept/$',views.BRadmin_project_dept,name='BRadmin_project_dept'), 
    re_path(r'^BRadmin_project_list/(?P<id>\d+)/$',views.BRadmin_project_list, name='BRadmin_project_list'),
    re_path(r'^BRadmin_project_table/(?P<id>\d+)/$', views.BRadmin_project_table,name='BRadmin_project_table'),
    # re_path(r'^accounts_internship_viewbydate/$', views.accounts_internship_viewbydate, name="accounts_internship_viewbydate"),
    
    # re_path(r'^accounts_internship_update/(?P<id>\d+)/$', views.accounts_internship_update, name="accounts_internship_update"),
    # re_path(r'^accounts_interndelete/(?P<id>\d+)/$', views.accounts_interndelete, name="accounts_interndelete"),
    # re_path(r'^accounts_internshipupdatesave/(?P<id>\d+)/$', views.accounts_internshipupdatesave, name="accounts_internshipupdatesave"),
    
    re_path(r'^accounts_internship_viewbydate/$', views.accounts_internship_viewbydate, name="accounts_internship_viewbydate"),
    
    re_path(r'^accounts_internship_update/(?P<id>\d+)/$', views.accounts_internship_update, name="accounts_internship_update"),
    re_path(r'^accounts_interndelete/(?P<id>\d+)/$', views.accounts_interndelete, name="accounts_interndelete"),
    re_path(r'^accounts_internshipupdatesave/(?P<id>\d+)/$', views.accounts_internshipupdatesave, name="accounts_internshipupdatesave"),    
    re_path(r'^trainer_save/(?P<id>\d+)$', views.trainer_save, name='trainer_save'),
    re_path(r'^projectmanager_workstatus/$', views.projectmanager_workstatus, name='projectmanager_workstatus'),
    re_path(r'^projectmanager_designation/$', views.projectmanager_designation, name='projectmanager_designation'),
    re_path(r'^projectmanager_emp_ajax/$', views.projectmanager_emp_ajax, name='projectmanager_emp_ajax'),
    re_path(r'^projectmanager_projects_details/$', views.projectmanager_projects_details, name='projectmanager_projects_details'),
   
   
    re_path( r'^pdfof/(?P<id>\d+)/', views.render_pdfof_view, name='pdfof'),
    re_path( r'^pdfre/(?P<id>\d+)/', views.render_pdfre_view, name='pdfre'),
    re_path( r'^pdfex/(?P<id>\d+)/', views.render_pdfex_view, name='pdfex'),
    re_path( r'^pdfau/(?P<id>\d+)/', views.render_pdfau_view, name='pdfau'),
    re_path(r'^admin_code$', views.admin_code, name='admin_code'),
    #******************reset password******************
    re_path(r'^reset_password/$', views.reset_password, name='reset_password'),
    
    
    #********************chritin account settings and change password***************
    re_path(r'^tlaccountset/$', views.tlaccountset, name='tlaccountset'),
    re_path(r'^imagechange_tl/(?P<id>\d+)/$', views.imagechange_tl, name='imagechange_tl'),
    re_path(r'^imagechange_pm/(?P<id>\d+)/$', views.imagechange_pm, name='imagechange_pm'),
    re_path(r'^imagechange_test/(?P<id>\d+)/$', views.imagechange_test, name='imagechange_test'),
    re_path(r'^imagechange_dev/(?P<id>\d+)/$', views.imagechange_dev, name='imagechange_dev'),
    re_path(r'^tlchangepass/$', views.tlchangepass, name='tlchangepass'),
    re_path(r'^prchangepass/$', views.prchangepass, name='prchangepass'),
    re_path(r'^testchangepass/$', views.testchangepass, name='testchangepass'),
    re_path(r'^devchangepass/$', views.devchangepass, name='devchangepass'),
    re_path(r'^pmaccountset/$', views.pmaccountset, name='pmaccountset'),
    re_path(r'^testaccountset/$', views.testaccountset, name='testaccountset'),
    re_path(r'^devaccountset/$', views.devaccountset, name='devaccountset'),


     #**********************super admin*************************
    
    re_path(r'^superadmin_index/$', views.superadmin_index, name="superadmin_index"),
    re_path(r'^superadmin_changepwd/$', views.superadmin_changepwd, name="superadmin_changepwd"),
    re_path(r'^superadmin_logout/$', views.superadmin_logout, name="superadmin_logout"),


#**************************Anandhu Super-Admin Dashboard section**************************
    re_path(r'^SuperAdmin_dashboard/$', views.SuperAdmin_dashboard, name='SuperAdmin_dashboard'),
    re_path(r'^SuperAdmin_profile/(?P<id>\d+)/$', views.SuperAdmin_profile, name='SuperAdmin_profile'),
    re_path(r'^SuperAdmin_trainersdepartment/(?P<id>\d+)/$', views.SuperAdmin_trainersdepartment, name='SuperAdmin_trainersdepartment'),
    re_path(r'^SuperAdmin_trainerstable/(?P<id>\d+)/$', views.SuperAdmin_trainerstable, name='SuperAdmin_trainerstable'),
    re_path(r'^SuperAdmin_trainerteams/(?P<id>\d+)/$', views.SuperAdmin_trainerteams, name='SuperAdmin_trainerteams'),
    re_path(r'^SuperAdmin_trainerteam/(?P<id>\d+)/$', views.SuperAdmin_trainerteam, name='SuperAdmin_trainerteam'),
    re_path(r'^SuperAdmin_topictable/(?P<id>\d+)/$', views.SuperAdmin_topictable, name='SuperAdmin_topictable'),
    re_path(r'^SuperAdmin_traineestable/(?P<id>\d+)/$', views.SuperAdmin_traineestable, name='SuperAdmin_traineestable'),
    re_path(r'^SuperAdmin_traineeprofile/(?P<id>\d+)/$', views.SuperAdmin_traineeprofile, name='SuperAdmin_traineeprofile'),
    re_path(r'^SuperAdmin_completedtasktable/(?P<id>\d+)/$', views.SuperAdmin_completedtasktable, name='SuperAdmin_completedtasktable'),
    
    
     # current projects-sharon -admin mod

    # re_path(r'^SuperAdmin_profiledash$', views.SuperAdmin_profiledash,name='SuperAdmin_profiledash'),
    re_path(r'^SuperAdmin_dept/(?P<id>\d+)/$', views.SuperAdmin_dept, name='SuperAdmin_dept'),
    re_path(r'^SuperAdmin_pythons$', views.SuperAdmin_pythons, name='SuperAdmin_pythons'),
    re_path(r'^SuperAdmin_projects/(?P<id>\d+)/$', views.SuperAdmin_projects, name='SuperAdmin_projects'),
    re_path(r'^SuperAdmin_proj_list/(?P<id>\d+)/$', views.SuperAdmin_proj_list, name='SuperAdmin_proj_list'),
    re_path(r'^SuperAdmin_proj_det/(?P<id>\d+)/$', views.SuperAdmin_proj_det, name='SuperAdmin_proj_det'),
    re_path(r'^SuperAdmin_proj_mngrs/(?P<id>\d+)/$', views.SuperAdmin_proj_mngrs, name='SuperAdmin_proj_mngrs'),
    re_path(r'^SuperAdmin_proj_mangrs1/(?P<id>\d+)/$', views.SuperAdmin_proj_mangrs1, name='SuperAdmin_proj_mangrs1'),
    re_path(r'^SuperAdmin_proj_mangrs2/(?P<id>\d+)/$', views.SuperAdmin_proj_mangrs2, name='SuperAdmin_proj_mangrs2'),  
    re_path(r'^SuperAdmin_daily_report/(?P<id>\d+)/$', views.SuperAdmin_daily_report, name='SuperAdmin_daily_report'),
    re_path(r'^SuperAdmin_developers/(?P<id>\d+)/$', views.SuperAdmin_developers, name='SuperAdmin_developers'),


# completed projects-subeeesh -admin mod

    re_path(r'^SuperAdmin_proj_cmpltd_new/(?P<id>\d+)/$', views.SuperAdmin_proj_cmpltd_new, name='SuperAdmin_proj_cmpltd_new'),
    re_path(r'^SuperAdmin_cmpltd_proj_det_new/(?P<id>\d+)/$', views.SuperAdmin_cmpltd_proj_det_new, name='SuperAdmin_cmpltd_proj_det_new'),
    re_path(r'^SuperAdmin_proj_mngrs_new/(?P<id>\d+)/$', views.SuperAdmin_proj_mngrs_new, name='SuperAdmin_proj_mngrs_new'),
    re_path(r'^SuperAdmin_proj_mangrs1_new/(?P<id>\d+)/$', views.SuperAdmin_proj_mangrs1_new, name='SuperAdmin_proj_mangrs1_new'),
    re_path(r'^SuperAdmin_proj_mangrs2_new/(?P<id>\d+)/$', views.SuperAdmin_proj_mangrs2_new, name='SuperAdmin_proj_mangrs2_new'),
    re_path(r'^SuperAdmin_developers_new/(?P<id>\d+)/$', views.SuperAdmin_developers_new, name='SuperAdmin_developers_new'),
    re_path(r'^SuperAdmin_daily_report_new/(?P<id>\d+)/$', views.SuperAdmin_daily_report_new, name='SuperAdmin_daily_report_new'),




    re_path(r'^SuperAdmin_employees/(?P<id>\d+)/$', views.SuperAdmin_employees, name='SuperAdmin_employees'),
    re_path(r'^SuperAdmin_edepartments/(?P<id>\d+)/$', views.SuperAdmin_edepartments, name='SuperAdmin_edepartments'),
    re_path(r'^SuperAdmin_projectman/(?P<id>\d+)/(?:(?P<did>\d+))?',views.SuperAdmin_projectman, name='SuperAdmin_projectman'),
    re_path(r'^SuperAdmin_ViewTrainers/(?P<id>\d+)/(?:(?P<did>\d+))?',views.SuperAdmin_ViewTrainers, name='SuperAdmin_ViewTrainers'),
    re_path(r'^SuperAdmin_View_Trainerprofile/(?P<id>\d+)/$', views.SuperAdmin_View_Trainerprofile, name='SuperAdmin_View_Trainerprofile'),
    re_path(r'^SuperAdmin_View_Currenttraineesoftrainer/(?P<id>\d+)/$', views.SuperAdmin_View_Currenttraineesoftrainer, name='SuperAdmin_View_Currenttraineesoftrainer'),
    re_path(r'^SuperAdmin_View_Currenttraineeprofile/(?P<id>\d+)/$', views.SuperAdmin_View_Currenttraineeprofile, name='SuperAdmin_View_Currenttraineeprofile'),
    re_path(r'^SuperAdmin_proname/(?P<id>\d+)/$', views.SuperAdmin_proname, name='SuperAdmin_proname'),
    re_path(r'^SuperAdmin_View_Currenttraineetasks/(?P<id>\d+)/$', views.SuperAdmin_View_Currenttraineetasks, name='SuperAdmin_View_Currenttraineetasks'),
    re_path(r'^SuperAdmin_ViewCurrenttraineeattendancesort/(?P<id>\d+)/$', views.SuperAdmin_ViewCurrenttraineeattendancesort, name='SuperAdmin_ViewCurrenttraineeattendancesort'),
    re_path(r'^SuperAdmin_View_Previoustraineesoftrainer/(?P<id>\d+)/$', views.SuperAdmin_View_Previoustraineesoftrainer, name='SuperAdmin_View_Previoustraineesoftrainer'),
    re_path(r'^SuperAdmin_View_Currenttraineeattendance/(?P<id>\d+)/$', views.SuperAdmin_View_Currenttraineeattendance, name='SuperAdmin_View_Currenttraineeattendance'),
    re_path(r'^SuperAdmin_View_Previoustraineeprofile/(?P<id>\d+)/$', views.SuperAdmin_View_Previoustraineeprofile, name='SuperAdmin_View_Previoustraineeprofile'),
    re_path(r'^SuperAdmin_View_Previoustraineetasks/(?P<id>\d+)/$', views.SuperAdmin_View_Previoustraineetasks, name='SuperAdmin_View_Previoustraineetasks'),
    re_path(r'^SuperAdmin_View_Previoustraineeattendance/(?P<id>\d+)/$', views.SuperAdmin_View_Previoustraineeattendance, name='SuperAdmin_View_Previoustraineeattendance'),
    re_path(r'^SuperAdmin_ViewPrevioustraineeattendancesort/(?P<id>\d+)/$', views.SuperAdmin_ViewPrevioustraineeattendancesort, name='SuperAdmin_ViewPrevioustraineeattendancesort'),
    re_path(r'^SuperAdmin_View_Trainerattendance/(?P<id>\d+)/$', views.SuperAdmin_View_Trainerattendance, name='SuperAdmin_View_Trainerattendance'),
    re_path(r'^SuperAdmin_proinvolve/(?P<id>\d+)/$', views.SuperAdmin_proinvolve, name='SuperAdmin_proinvolve'),
    re_path(r'^SuperAdmin_ViewTrainerattendancesort/(?P<id>\d+)/$', views.SuperAdmin_ViewTrainerattendancesort, name='SuperAdmin_ViewTrainerattendancesort'),
    re_path(r'^SuperAdmin_promanatten/(?P<id>\d+)/$', views.SuperAdmin_promanatten, name='SuperAdmin_promanatten'),
    re_path(r'^SuperAdmin_promanattendsort/(?P<id>\d+)/$', views.SuperAdmin_promanattendsort, name='SuperAdmin_promanattendsort'),




    re_path(r'^SuperAdmin_admin_registration/$', views.SuperAdmin_admin_registration, name='SuperAdmin_admin_registration'),
    re_path(r'^SuperAdmin_registration/$', views.SuperAdmin_registration, name='SuperAdmin_registration'),
    re_path(r'^SuperAdmin_Add/$', views.SuperAdmin_Add, name='SuperAdmin_Add'),


    re_path(r'^SuperAdmin_admin_view$', views.SuperAdmin_admin_view, name='SuperAdmin_admin_view'),

    re_path(r'^admindelete/(?P<id>\d+)/$', views.admindelete, name='admindelete'),

    re_path(r'^SuperAdmin_admin_update/(?P<id>\d+)/$', views.SuperAdmin_admin_update, name='SuperAdmin_admin_update'),

    re_path(r'^SuperAdmin_updatesave/(?P<id>\d+)/$', views.SuperAdmin_updatesave, name='SuperAdmin_updatesave'),
   
    



    re_path(r'^SuperAdmin_Branch$', views.SuperAdmin_Branch, name='SuperAdmin_Branch'),
    re_path(r'^SuperAdmin_AddBranch$', views.SuperAdmin_AddBranch, name='SuperAdmin_AddBranch'),


    re_path(r'^SuperAdmin_Viewbranch/$', views.SuperAdmin_Viewbranch, name='SuperAdmin_Viewbranch'),
    re_path(r'^SuperAdmin_Updatebranch/(?P<id>\d+)/$', views.SuperAdmin_Updatebranch, name='SuperAdmin_Updatebranch'),  
    re_path(r'^SuperAdmin_branchupdate/(?P<id>\d+)/$', views.SuperAdmin_branchupdate, name='SuperAdmin_branchupdate'), 
    re_path(r'^SuperAdmin_Branchdelete/(?P<id>\d+)/$', views.SuperAdmin_Branchdelete, name='SuperAdmin_Branchdelete'),



    re_path(r'^SuperAdminreply/(?P<id>\d+)/$', views.SuperAdminreply, name="SuperAdminreply"),
    re_path(r'^SuperAdmin_Reportedissue_department$',views.SuperAdmin_Reportedissue_department, name='SuperAdmin_Reportedissue_department'),
    re_path(r'^SuperAdmin_ReportedissueShow/(?P<id>\d+)/$',views.SuperAdmin_ReportedissueShow, name='SuperAdmin_ReportedissueShow'),
    
    ########## end ##########
    
    # Error fix
    re_path(r'^accounts_traineepayment_notverified/$', views.accounts_traineepayment_notverified, name='accounts_traineepayment_notverified'),
    re_path(r'^verified/(?P<id>\d+)$',views.verified,name="verified"), 
    re_path(r'^accounts_traineepayment_pending/$', views.accounts_traineepayment_pending,name='accounts_traineepayment_pending'),
    re_path(r'^accounts_newtrainees/$', views.accounts_newtrainees,name='accounts_newtrainees'),
    re_path(r'^accounts_salary_employees/$',views.accounts_salary_employees, name='accounts_salary_employees'),
    re_path(r'^accounts_salaryconfirm/(?P<id>\d+)$', views.accounts_salaryconfirm, name='accounts_salaryconfirm'),
    re_path(r'^accounts_salaried_employees/$', views.accounts_salaried_employees, name='accounts_salaried_employees'),
    re_path(r'^accounts_monthdays_cards/$',views.accounts_monthdays_cards,name="accounts_monthdays_cards"),
    re_path(r'^accounts_month_adddays_form/$',views.accounts_month_adddays_form,name="accounts_month_adddays_form"),
    re_path(r'^accounts_month_viewdays/$',views.accounts_month_viewdays,name="accounts_month_viewdays"),
    
    re_path(r'^SuperAdmin_leavehistory$',views.SuperAdmin_leavehistory,name="SuperAdmin_leavehistory"),
    re_path(r'^SuperAdmin_leaveapprovedstatus/(?P<id>\d+)/$',views.SuperAdmin_leaveapprovedstatus,name="SuperAdmin_leaveapprovedstatus"),
    re_path(r'^SuperAdmin_rejectedstatus/(?P<id>\d+)/$',views.SuperAdmin_rejectedstatus,name="SuperAdmin_rejectedstatus"),

    re_path(r'^projectMAN_leavehistory$',views.projectMAN_leavehistory,name="projectMAN_leavehistory"),     
    re_path(r'^projectMAN_leaveapprovedstatus/(?P<id>\d+)/$',views.projectMAN_leaveapprovedstatus,name="projectMAN_leaveapprovedstatus"),
    re_path(r'^projectMAN_rejectedstatus/(?P<id>\d+)/$',views.projectMAN_rejectedstatus,name="projectMAN_rejectedstatus"),

    re_path(r'^TL_leavehistory$',views.TL_leavehistory,name="TL_leavehistory"),       
    re_path(r'^TL_leaveapprovedstatus/(?P<id>\d+)/$',views.TL_leaveapprovedstatus,name="TL_leaveapprovedstatus"),
    re_path(r'^TL_rejectedstatus/(?P<id>\d+)/$',views.TL_rejectedstatus,name="TL_rejectedstatus"),
    
    re_path(r'^trainer_leavehistory/$',views.trainer_leavehistory,name="trainer_leavehistory"),
    re_path(r'^trainer_leaveapprovedstatus/(?P<id>\d+)/$',views.trainer_leaveapprovedstatus,name="trainer_leaveapprovedstatus"),
    re_path(r'^trainer_rejectedstatus/(?P<id>\d+)/$',views.trainer_rejectedstatus,name="trainer_rejectedstatus"),

    re_path(r'^tm_leavehistory/$',views.tm_leavehistory,name="tm_leavehistory"),       
    re_path(r'^tm_leaveapprovedstatus/(?P<id>\d+)/$',views.tm_leaveapprovedstatus,name="tm_leaveapprovedstatus"),
    re_path(r'^tm_rejectedstatus/(?P<id>\d+)/$',views.tm_rejectedstatus,name="tm_rejectedstatus"),
    

    re_path(r'^BRadmin_leavehistory/$',views.BRadmin_leavehistory,name="BRadmin_leavehistory"),         
    re_path(r'^BRadmin_leaveapprovedstatus/(?P<id>\d+)/$',views.BRadmin_leaveapprovedstatus,name="BRadmin_leaveapprovedstatus"),
    re_path(r'^BRadmin_rejectedstatus/(?P<id>\d+)/$',views.BRadmin_rejectedstatus,name="BRadmin_rejectedstatus"),
    
    # re_path(r'^accounts_account_salary/$',views.accounts_account_salary,name="accounts_account_salary"),
    # re_path(r'^accounts_accout_salary_slip/(?P<id>\d+)/$',views.accounts_accout_salary_slip,name="accounts_accout_salary_slip"),
    # re_path(r'^accounts_salary_pending/$', views.accounts_salary_pending, name='accounts_salary_pending'),
    # re_path(r'^salarysubmit/(?P<id>\d+)$', views.salarysubmit, name='salarysubmit'),
    # re_path(r'^accounts_salary_given/$',views.accounts_salary_given, name='accounts_salary_given'),
    # re_path(r'^accounts_promissory/(?P<id>\d+)/$', views.accounts_promissory, name='accounts_promissory'),
    # re_path(r'^accounts_download_promissory/(?P<id>\d+)/$', views.accounts_download_promissory, name='accounts_download_promissory'),
    # re_path(r'^accounts_promissory_complete_pfd/(?P<id>\d+)/$', views.accounts_promissory_complete_pfd, name='accounts_promissory_complete_pfd'),
    # re_path(r'^accounts_promissory_notcomplete_pfd/(?P<id>\d+)/$', views.accounts_promissory_notcomplete_pfd, name='accounts_promissory_notcomplete_pfd'),
    # re_path(r'^accounts_promissory_add/(?P<id>\d+)/$', views.accounts_promissory_add, name='accounts_promissory_add'),
    # re_path(r'^accounts_workstatus/$', views.accounts_workstatus, name='accounts_workstatus'),
    # re_path(r'^accounts_designation/$', views.accounts_designation, name='accounts_designation'),
    # re_path(r'^accounts_emp_ajax/$', views.accounts_emp_ajax, name='accounts_emp_ajax'),
    # re_path(r'^accounts_project_details/$', views.accounts_project_details, name='accounts_project_details'),
    # re_path(r'^accounts_add_bank_acnt_update/(?P<id>\d+)/$', views.accounts_add_bank_acnt_update, name='accounts_add_bank_acnt_update'),
    
re_path(r'^accounts_account_salary/$',views.accounts_account_salary,name="accounts_account_salary"),
    re_path(r'^accounts_accout_salary_slip/(?P<id>\d+)/$',views.accounts_accout_salary_slip,name="accounts_accout_salary_slip"),
    re_path(r'^accounts_salary_pending/$', views.accounts_salary_pending, name='accounts_salary_pending'),
    re_path(r'^salarysubmit/(?P<id>\d+)$', views.salarysubmit, name='salarysubmit'),
    re_path(r'^accounts_salary_given/$',views.accounts_salary_given, name='accounts_salary_given'),
    re_path(r'^accounts_promissory/(?P<id>\d+)/$', views.accounts_promissory, name='accounts_promissory'),
    re_path(r'^accounts_download_promissory/(?P<id>\d+)/$', views.accounts_download_promissory, name='accounts_download_promissory'),
    re_path(r'^accounts_promissory_complete_pfd/(?P<id>\d+)/$', views.accounts_promissory_complete_pfd, name='accounts_promissory_complete_pfd'),
    re_path(r'^accounts_promissory_notcomplete_pfd/(?P<id>\d+)/$', views.accounts_promissory_notcomplete_pfd, name='accounts_promissory_notcomplete_pfd'),
    re_path(r'^accounts_promissory_add/(?P<id>\d+)/$', views.accounts_promissory_add, name='accounts_promissory_add'),
    re_path(r'^accounts_workstatus/$', views.accounts_workstatus, name='accounts_workstatus'),
    re_path(r'^accounts_designation/$', views.accounts_designation, name='accounts_designation'),
    re_path(r'^accounts_emp_ajax/$', views.accounts_emp_ajax, name='accounts_emp_ajax'),
    re_path(r'^accounts_project_details/$', views.accounts_project_details, name='accounts_project_details'),
    re_path(r'^accounts_add_bank_acnt_update/(?P<id>\d+)/$', views.accounts_add_bank_acnt_update, name='accounts_add_bank_acnt_update'),
    
    
    re_path(r'^test/(?P<id>\d+)/$', views.test, name='test'),
    re_path(r'^DEVpayments/$', views.DEVpayments, name="DEVpayments"),
    re_path(r'^TLpayment/$', views.TLpayment, name="TLpayment"),
    re_path(r'^trainingmanager_payment_list/$',views.trainingmanager_payment_list, name="trainingmanager_payment_list"),
    re_path(r'^paypdf/(?P<id>\d+)/(?P<tid>\d+)/$', views.paypdf,name="paypdf"),
    re_path(r'^trainer_payment_list/$',views.trainer_payment_list, name="trainer_payment_list"),
    re_path(r'^MAN_payment_list/$',views.MAN_payment_list, name="MAN_payment_list"),
    re_path(r'^projectmanager_payment_list/',views.projectmanager_payment_list, name="projectmanager_payment_list"),
    
    re_path(r'^project_reset/(?P<id>\d+)/$', views.project_reset, name='project_reset'),
    
    re_path(r'^projectmanager_trainee_status$', views.projectmanager_trainee_status, name='projectmanager_trainee_status'),
    re_path(r'^projectmanager_trainee_details$', views.projectmanager_trainee_details, name='projectmanager_trainee_details'),
    
    # *************************HR MODULE*******************************

     re_path(r'^HR_Dashboard/$', views.HR_Dashboard, name='HR_Dashboard'),
     re_path(r'^HR_leave/$', views.HR_leave, name='HR_leave'),
     re_path(r'^HR_leaveapply/$', views.HR_leaveapply, name='HR_leaveapply'),
     re_path(r'^HR_appliedleave/$', views.HR_appliedleave, name='HR_appliedleave'),
     re_path(r'^HR_issue/$', views.HR_issue, name='HR_issue'),
     re_path(r'^HR_reportissue/$', views.HR_reportissue, name='HR_reportissue'),
     re_path(r'^HR_reportedissue/$', views.HR_reportedissue, name='HR_reportedissue'),
     re_path(r'^HR_trainingdepartment/$', views.HR_trainingdepartment, name='HR_trainingdepartment'),
     re_path(r'^HR_trainerslist/(?P<id>\d+)/$', views.HR_trainerslist, name='HR_trainerslist'),
     re_path(r'^HR_trainersteam/(?P<id>\d+)/$', views.HR_trainersteam, name='HR_trainersteam'),
     re_path(r'^HR_trainersteamdetails/(?P<id>\d+)/$', views.HR_trainersteamdetails, name='HR_trainersteamdetails'),
     re_path(r'^HR_trainees/(?P<id>\d+)/$', views.HR_trainees, name='HR_trainees'),
     re_path(r'^HR_traineestopic/(?P<id>\d+)/$', views.HR_traineestopic, name='HR_traineestopic'),
     re_path(r'^HR_traineeprofile/(?P<id>\d+)/$', views.HR_traineeprofile, name='HR_traineeprofile'),
     re_path(r'^HR_traineecompletedtask/(?P<id>\d+)/$', views.HR_traineecompletedtask, name='HR_traineecompletedtask'),
     re_path(r'^HR_employeesdepartment/$', views.HR_employeesdepartment, name='HR_employeesdepartment'),
     re_path(r'^HR_employeeslist/(?P<id>\d+)/$', views.HR_employeeslist, name='HR_employeeslist'),
     re_path(r'^HR_viewtrainers/(?P<id>\d+)/(?:(?P<did>\d+))?', views.HR_viewtrainers, name='HR_viewtrainers'),
     re_path(r'^HR_trainerprofile/(?P<id>\d+)/$', views.HR_trainerprofile, name='HR_trainerprofile'),
     re_path(r'^HR_trainercurrenttrainees/(?P<id>\d+)/$', views.HR_trainercurrenttrainees, name='HR_trainercurrenttrainees'),
     re_path(r'^HR_trainerprevioustrainees/(?P<id>\d+)/$', views.HR_trainerprevioustrainees, name='HR_trainerprevioustrainees'),
     re_path(r'^HR_trainersattendance/(?P<id>\d+)/$', views.HR_trainersattendance, name='HR_trainersattendance'),
     re_path(r'^HR_trainersattendanceview/(?P<id>\d+)/$', views.HR_trainersattendanceview, name='HR_trainersattendanceview'),
     re_path(r'^HR_employeedetails/(?P<id>\d+)/(?:(?P<did>\d+))?', views.HR_employeedetails, name='HR_employeedetails'),
     re_path(r'^HR_employeesprofile/(?P<id>\d+)/$', views.HR_employeesprofile, name='HR_employeesprofile'),
     re_path(r'^HR_employeesinvolvedprojects/(?P<id>\d+)/(?:(?P<did>\d+))?', views.HR_employeesinvolvedprojects, name='HR_employeesinvolvedprojects'),
     re_path(r'^HR_employeesattendance/(?P<id>\d+)/$', views.HR_employeesattendance, name='HR_employeesattendance'),
     re_path(r'^HR_employeesattendancesort/(?P<id>\d+)/$', views.HR_employeesattendancesort, name='HR_employeesattendancesort'),
     re_path(r'^HR_changepassword/$', views.HR_changepassword, name='HR_changepassword'),
     re_path(r'^HR_accountsettings/$', views.HR_accountsettings, name='HR_accountsettings'),
     re_path(r'^HR_imagesettings/$', views.HR_imagesettings, name='HR_imagesettings'),
     re_path(r'^HR_logout/$', views.HR_logout, name='HR_logout'),  
     
    re_path(r'^completedteam/$', views.completedteam, name='completedteam'),
    re_path(r'^completed_team_trainees/(?P<id>\d+)/$', views.completed_team_trainees, name='completed_team_trainees'),
    re_path(r'^completed_team_task/(?P<id>\d+)/(?P<tid>\d+)/$', views.completed_team_task, name='completed_team_task'),
    re_path(r'^probations/$', views.probations, name='probations'),
    re_path(r'^task_perform$', views.task_perform, name='task_perform'),
    re_path(r'^probation_stop/$', views.probation_stop, name='probation_stop'),
    re_path(r'^probation_renew/$', views.probation_renew, name='probation_renew'),
    re_path(r'^tm_trainee_status$', views.tm_trainee_status, name='tm_trainee_status'),
    re_path(r'^tm_trainee_details$', views.tm_trainee_details, name='tm_trainee_details'),

    re_path(r'^manager_trainee_status$', views.manager_trainee_status, name='manager_trainee_status'),
    re_path(r'^manager_trainee_details$', views.manager_trainee_details, name='manager_trainee_details'),
    re_path(r'^manager_trainess$', views.manager_trainess, name='manager_trainess'),

      
    re_path(r'^BRadmin_trainee_status$', views.BRadmin_trainee_status, name='BRadmin_trainee_status'),
    re_path(r'^BRadmin_trainee_details$', views.BRadmin_trainee_details, name='BRadmin_trainee_details'),
    re_path(r'^BRadmin_trainess$', views.BRadmin_trainess, name='BRadmin_trainess'),
    re_path(r'^BRadmin_leavestatus/$', views.BRadmin_leavestatus, name='BRadmin_leavestatus'),
    re_path(r'^BRadmin_leavedesgn/$', views.BRadmin_leavedesgn, name='BRadmin_leavedesgn'),

    re_path(r'^BRadmin_leave_details/$', views.BRadmin_leave_details, name='BRadmin_leave_details'),
    re_path(r'^pm_projectcards/$', views.pm_projectcards, name='pm_projectcards'),
    re_path(r'^pm_createmodule/$', views.pm_createmodule, name='pm_createmodule'),
    re_path(r'^pm_createtable/$', views.pm_createtable, name='pm_createtable'),
    re_path(r'^pm_module_data/$', views.pm_module_data, name='pm_module_data'),
    re_path(r'^pm_projectview/$', views.pm_projectview, name='pm_projectview'),
    re_path(r'^pm_prodata/(?P<id>\d+)/$', views.pm_prodata, name='pm_prodata'),
    re_path(r'^pm_project_assigned/(?P<id>\d+)/$', views.pm_project_assigned, name='pm_project_assigned'),
    re_path(r'^trainer_progress_add/(?P<id>\d+)/$', views.trainer_progress_add, name='trainer_progress_add'),
    re_path(r'^tester_leave/$', views.tester_leave, name='tester_leave'),
    re_path(r'^tester_apply_leave/$', views.tester_apply_leave, name='tester_apply_leave'),
    re_path(r'^tester_appliedleave/$', views.tester_appliedleave, name='tester_appliedleave'),
    re_path(r'^projectman_search/$', views.projectman_search, name='projectman_search'),
    re_path(r'^pm_employees_att/$', views.pm_employees_att, name='pm_employees_att'),
    re_path(r'^pm_attendanceview/$', views.pm_attendanceview, name='pm_attendanceview'),
    re_path(r'^pm_employeelist/$', views.pm_employeelist, name='pm_employeelist'),
    re_path(r'^pm_employees_attendance_view/$', views.pm_employees_attendance_view, name='pm_employees_attendance_view'),
    re_path(r'^tl_attendanceview/$', views.tl_attendanceview, name='tl_attendanceview'),
    re_path(r'^tl_devattendanceview/$', views.tl_devattendanceview, name='tl_devattendanceview'),
    re_path(r'^tl_devattendanceadd/$', views.tl_devattendanceadd, name='tl_devattendanceadd'),
    re_path(r'^tl_employees_att/$', views.tl_employees_att, name='tl_employees_att'),
    re_path(r'^tl_add_attendance/(?P<id>\d+)/$', views.tl_add_attendance, name='tl_add_attendance'),
    re_path(r'^pm_add_attendance/(?P<id>\d+)/$', views.pm_add_attendance, name='pm_add_attendance'),
    re_path(r'^tester_employees/$', views.tester_employees, name='tester_employees'),
    re_path(r'^tester_tllist/$', views.tester_tllist, name='tester_tllist'),
    re_path(r'^tester_tldashboard/(?P<id>\d+)/$', views.tester_tldashboard, name='tester_tldashboard'),
    re_path(r'^ts_ltteaminvolved/(?P<id>\d+)/$', views.ts_ltteaminvolved, name='ts_ltteaminvolved'),
    re_path(r'^tl_currentperformance/(?P<id>\d+)/$', views.tl_currentperformance, name='tl_currentperformance'),
    re_path(r'^ts_allocatetl/$', views.ts_allocatetl, name='ts_allocatetl'),
    re_path(r'^ts_tl_attendance/(?P<id>\d+)/$', views.ts_tl_attendance, name='ts_tl_attendance'),
    re_path(r'^ts_tl_attandance/(?P<id>\d+)/$', views.ts_tl_attandance, name='ts_tl_attandance'),
    re_path(r'^tl_devattendsearch/$', views.tl_devattendsearch, name='tl_devattendsearch'),
    re_path(r'^ts_dev_team/(?P<id>\d+)/$', views.ts_dev_team, name='ts_dev_team'),
    re_path(r'^ts_dev_team_profile/(?P<id>\d+)/$', views.ts_dev_team_profile, name='ts_dev_team_profile'),
    re_path(r'^ts_tl_dev_teaminvolved/(?P<id>\d+)/$', views.ts_tl_dev_teaminvolved, name='ts_tl_dev_teaminvolved'),
    re_path(r'^ts_Devlists/$', views.ts_Devlists, name='ts_Devlists'),
    re_path(r'^ts_DevDashboard/(?P<id>\d+)/$', views.ts_DevDashboard, name='ts_DevDashboard'),
    re_path(r'^current_modules/(?P<id>\d+)/$', views.current_modules, name='current_modules'),    
    
    
    re_path(r'^calendar$', calviews.CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', calviews.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', calviews.event, name='event_edit'),
    
    
    re_path(r'^accounts_salary_leave/$', views.accounts_salary_leave, name='accounts_salary_leave'),
     

    
    # re_path(r'^static/(?P<path>*)$', serve,{'document_root':settings.STATIC_ROOT}),
    #re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^acntpaypdf/(?P<id>\d+)/(?P<tid>\d+)/$', views.acntpaypdf, name='acntpaypdf'),
    re_path(r'^paypdf/(?P<id>\d+)/(?P<tid>\d+)/$', views.paypdf,name="paypdf"),
    
    re_path(r'^accounts_leave/$', views.accounts_leave, name='accounts_leave'),
    re_path(r'^pm_leavestatus/$', views.pm_leavestatus, name='pm_leavestatus'),
    re_path(r'^pm_leave/$', views.pm_leave, name='pm_leave'),
    
    
    
    
    re_path(r'^accounts_paymenthead/$', views.accounts_paymenthead, name='accounts_paymenthead'),
    re_path(r'^accounts_addpaymenthead/$', views.accounts_addpaymenthead, name='accounts_addpaymenthead'),
    re_path(r'^accounts_viewpaymenthead/$', views.accounts_viewpaymenthead, name='accounts_viewpaymenthead'),
    re_path(r'^accounts_income/$', views.accounts_income, name='accounts_income'),
    re_path(r'^accounts_addincome/$', views.accounts_addincome, name='accounts_addincome'),
    re_path(r'^accounts_viewallincome/$', views.accounts_viewallincome, name='accounts_viewallincome'),
    re_path(r'^accounts_filterincome/$', views.accounts_filterincome, name='accounts_filterincome'),
    re_path(r'^accounts_filterincome_ajax/$', views.accounts_filterincome_ajax, name='accounts_filterincome_ajax'),
   
    re_path(r'^BRadmin_income/$', views.BRadmin_income, name='BRadmin_income'),
    re_path(r'^BRadmin_viewallincome/$', views.BRadmin_viewallincome, name='BRadmin_viewallincome'),
    re_path(r'^BRadmin_pendingincome/$', views.BRadmin_pendingincome, name='BRadmin_pendingincome'),
    re_path(r'^BRadmin_searchincome/$', views.BRadmin_searchincome, name='BRadmin_searchincome'),
    re_path(r'^BRadmin_filterincome_ajax/$', views.BRadmin_filterincome_ajax, name='BRadmin_filterincome_ajax'),


    re_path(r'^accounts_mainexpenses/$', views.accounts_mainexpenses, name='accounts_mainexpenses'),
    re_path(r'^accounts_salaryexpense/$', views.accounts_salaryexpense, name='accounts_salaryexpense'),
    re_path(r'^accounts_salaryexpense_ajax/$', views.accounts_salaryexpense_ajax, name='accounts_salaryexpense_ajax'),

    re_path(r'^BRadmin_mainexpenses/$', views.BRadmin_mainexpenses, name='BRadmin_mainexpenses'),
    re_path(r'^BRadmin_salaryexpense/$', views.BRadmin_salaryexpense, name='BRadmin_salaryexpense'),
    re_path(r'^verify_all_income/$', views.verify_all_income, name='verify_all_income'),



    re_path(r'^Teamdevelopers/$', views.TL_dev, name='TL_dev'),
    re_path(r'^Teamdevelopers_dashboard/(?P<id>\d+)/$', views.Teamdevelopers_dashboard, name='Teamdevelopers_dashboard'),
    re_path(r'^TL_add_dev_performance/(?P<id>\d+)/$', views.TL_add_dev_performance, name='TL_add_dev_performance'),


    re_path(r'^tm_leave_status/$', views.tm_leave_status, name='tm_leave_status'),
    re_path(r'^tm_designation/$', views.tm_designation, name='tm_designation'),
    re_path(r'^tm_emp_ajax/$', views.tm_emp_ajax, name='tm_emp_ajax'),
    re_path(r'^tm_leave/$', views.tm_leave, name='tm_leave'),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
