from time import sleep

from common.driver import DriverOperate

from pages.page_send_email import PageSendEmail

class SendEmailActions:
    def SendEmail(self, address, theme, body):
        page = PageSendEmail()

        page.page_click_write_email()
        sleep(2)
        page.page_input_receiver(address)
        sleep(2)
        page.page_input_theme(theme)
        sleep(2)
        page.page_enter_body_frame()
        sleep(2)
        page.page_input_body(body)
        sleep(2)
        page.switch_frame_to_default()
        sleep(2)
        page.page_click_send()
        sleep(3)
