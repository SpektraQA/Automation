

XPATH_LOCATORS = [
    "//button[text()='Sign up']",  # кнопка "Sign up" на главной странице",
    "//button[text()='Sign In']",  # кнопка "Sign In" на главной странице",
    "//button[text()='Guest log in']",  # кнопка "Guest log in'" на главной странице",
    "//button[text()='Contacts']", # кнопка "Contacts" на главной странице",
    "//button[text()='About']",
    "//a[contains(text(), 'Home')]",
    "//*[text()='Instructions and manuals']",
    "//*[text()='Watch over 100 instructions and repair your car yourself.']",
    "//img[@src='/assets/images/homepage/info_1.jpg']", # картинка с 'Fuel Expenses'
    "//img[@src='/assets/images/homepage/info_2.jpg']",
    "//*[@href='https://www.facebook.com/Hillel.IT.School']", # переход на Facebook школы
    "//*[@href='https://t.me/ithillel_kyiv']",
    "//*[@href='https://www.youtube.com/user/HillelITSchool?sub_confirmation=1']",
    "//*[@href='https://www.instagram.com/hillel_itschool/']",
    "//*[@href='https://www.linkedin.com/school/ithillel/']",
    "//*[@href='https://ithillel.ua']", # главная страница школы
    "//nav[@class='header_nav d-flex align-items-center']//a[text()='Home']", # первый составной
    "//nav[contains(@class,'header_nav')]/button[text()='About']",
    "//nav[contains(@class,'header_nav')]/button[text()='Contacts']",
    "//div[@class='app-wrapper']//nav[contains(@class,'header_nav')]",
    "//div[@class='app-wrapper']//a[contains(@class, 'header_logo')]",
    "//div[@id='aboutSection']//div[contains(@class, 'container')]",
    "//header[@class='header bg-basic-dark']//div[contains(@class, 'container')]",
    "//div[@class='app-wrapper']//h1[contains(@class, 'hero-descriptor_title display-2')]",
    "//header[@class='header bg-basic-dark']//a[contains(@class, 'btn header-link -active')]",
]

CSS_LOCATORS = [
    "button.btn-primary",
    "#contactsSection .contacts_link",
    "#contactsSection .socials_link",
    "a.contacts_link[href^='mailto:']",
    "a.contacts_link.display-4[href^='https://ithillel.ua']",
    "a.socials_link[href^='https://www.instagram.com/hillel_itschool/']",
    "iframe.hero-video_frame",
    ".hero-descriptor_descr.lead",
    ".hero-descriptor_btn.btn.btn-primary",
    ".section.about",
    ".col-12.col-lg-6",
    ".col-12.col-lg-6.mt-lg-0.mt-md-5.mt-sm-4.mt-3",
    ".about-block_title.h2",
    "#contactsSection .row",
    "#contactsSection .contacts_socials.socials",
    "#contactsSection .socials_icon.icon.icon-facebook",
    "#contactsSection .socials_icon.icon.icon-telegram",
    "#contactsSection .socials_icon.icon.icon-youtube",
    "#player-controls .new-controls.bigbar",
    "#player-control-overlay",
    ".player-controls-middle-core-buttons",
    "#goog-gt-votingHiddenPane",
    ".ytp-player-content .ytp-timely-actions-content",
    ".ytp-caption-window-container",
    ".ytPlayerControlsContainerHost.ytPlayerControlsContainerRendered",
]