from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('profile/',profile,name="profile"),
    path('profile/upload/staff/',staff_profile,name="staff_profile"),
    path('profile/upload/student/3/',student_profile_3,name="student_profile_3"),
    path('profile/upload/company/2/',company_profile_2,name="company_profile_2"),
    path('profile/upload/company/3/',company_profile_3,name="company_profile_3"),
    path('profile/upload/student/2/',student_profile_2,name="student_profile_2"),
    path('profile/upload/student/1/',student_profile_1,name="student_profile_1"),
    path('profile/upload/phone_number/',student_company_number,name="student_company_number"),
    path('profile/changepassword/',change_password,name="change_password"),
    path('send/otp/phone/student/',send_otp_to_phone_stu,name="send_otp_to_phone_stu"),
    path('send/otp/phone/student/verify/',verify_otp_phone_stu,name="verify_otp_phone_stu"),
    path('resend/otp/phone/student/',resend_otp_to_phone_stu,name="resend_otp_to_phone_stu"),
    path('send/otp/phone/company/',send_otp_to_phone_com,name="send_otp_to_phone_com"),
    path('send/otp/phone/compnay/verify/',verify_otp_phone_com,name="verify_otp_phone_com"),
    path('resend/otp/phone/company/',resend_otp_to_phone_com,name="resend_otp_to_phone_com"),
    path('profile/skip/phonenumber/',skip_profile_phonenumber,name="skip_profile_phonenumber"),
    
    path('permit/signup_request/student/',student_account_signup_permit,name="student_account_signup_permit"),
    path('permit/signup_request/student/<str:type>/<str:item>',student_account_signup_action,name="student_account_signup_action"),
    path('permit/signup_request/company/',company_account_signup_permit,name="company_account_signup_permit"),
    path('permit/signup_request/company/<str:type>/<str:item>',company_account_signup_action,name="company_account_signup_action"),
    path('announcement/new/round/',new_announcement_round,name="new_announcement_round"),
    path('announcement/new/',new_announcement,name="new_announcement"),
    path('announcement/new/success/<str:item>',new_announcement_success,name="new_announcement_success"),
    path('announcements/',announcements,name="announcements"),
    path('announcements/edit/<str:item>/',edit_announcement,name="edit_announcement"),
    path('announcements/result/<str:item>', stu_result, name="stu_result"),
    path('announcements/result/file/upload/<str:item>',students_result_file_upload,name="students_result_file_upload"),
    path('register/company/',show_companies,name="show_companies"),
    path('show/company/details/<str:item>',show_company_round_details,name="show_company_round_details"),
    path('register/company/round/1/id/<str:item>',register_student_first_round_only,name="register_student_first_round_only"),
    path('show/student/registrations/all/',show_registrations,name="show_registrations"),
    path('announcements/internship/',announce_internship,name="announce_internship"),    
    path('show/internships/all/',internships,name="internships"),
    path('internships/edit/<str:item>',edit_internship,name="edit_internship"),
    path('internships/delete/<str:item>',delete_internship,name="delete_internship"),
    path('announcement/delete/<str:item>',delete_announcement,name="delete_announcement"),
    path('profile/student/<str:item>',check_student_profile,name="check_student_profile"),
    path('profile/company/<str:item>',check_company_profile,name="check_company_profile"),
    path('profile/company/change/mode/<str:item>',company_change_mode,name="company_change_mode"),
    path('profile/staff/<str:item>',check_staff_profile,name="check_staff_profile"),
    path('results/seeze/<str:item>',seeze_results,name="seeze_results"),
    path('internships/result/<str:item>',internship_result,name="internship_result"),
    path('staff/restrict/users/',restrict_users,name="restrict_users"),
    path('staff/restrict/user/permanent/<str:item>',ban_user_account_permanent,name="ban_user_account_permanent"),
    path('staff/restrict/staff/delete/account/<str:item>/<str:type>',delete_staff_account_admin,name="delete_staff_account_admin"),
    path('staff/restrict/user/temporary/<str:item>',ban_user_account_temporary,name="ban_user_account_temporary"),
    path('staff/unrestrict/user/<str:item>',unban_user,name="unban_user"),

    path('staff/create/accounts/',create_accounts,name="create_accounts"),
    path('staff/manage/blogs/',manage_blogs,name="manage_blogs"),
    path('staff/manage/blogs/new/',create_new_blog,name="create_new_blog"),
    path('staff/manage/blog/delete/<str:item>',delete_blog,name="delete_blog"),
    path('staff/manage/blog/edit/<str:item>',edit_blog,name="edit_blog"),
    path('admin/manage/staff/accounts/',manage_staff_accounts,name="manage_staff_accounts"),
    path('admin/manage/staff/account/edit/str:<item>',edit_staff_permissions,name="edit_staff_permissions"),
    path('admin/manage/staff/new/account/',create_new_staff_account,name="create_new_staff_account"),
    # path('student/action/internship/<str:item>/<str:type>',internship_action,name="internship_action"),
    path('notifications/all/',notifications,name="notifications"),
    path('notifications/float/',give_notifications,name="give_notifications"),
    path('notifications/my/delete/<str:item>',notification_delete,name="notification_delete"),
    
    path('chat_support/all/',all_chats,name="all_chats"),
    path('chat/visit/<str:item>',visit_chat,name="visit_chat"),
    path('chat/send/<str:item>',send_chat,name="send_chat"),
    path('chat/receive/<str:item>',receive_chat,name="receive_chat"),
    path('chat/end/<str:item>',end_chat,name="end_chat"),
    path('chat/change/mode/<str:item>',change_chat_mode,name="change_chat_mode"),

    path('technical_support/assist/',technical_support_assist,name="technical_support_assist"),

    path('account/delete/',delete_account,name="delete_account"),
    path('search/users/',search_users,name="search_users"),
    path('manage/sessions/',manage_sessions,name="manage_sessions"),
    path('manage/sessions/get/result/<str:item>',manage_sessions_get_result,name="manage_sessions_get_result"),
    path('remove/students/',remove_students,name="remove_students"),
    path('remove/companies/',remove_companies,name="remove_companies"),
    path('upload/cgpa/',upload_cgpa,name="upload_cgpa"),
    path('manage/company/internships/',manage_company_internships,name="manage_company_internships"),
    path('manage/company/internships/enter/<str:item>',login_as_a_company,name="login_as_a_company"),
]