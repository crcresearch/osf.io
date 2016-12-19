<%!
    from website import settings
%>

Hello ${user.fullname},

${referrer_name + ' has added you' if referrer_name else 'You have been added'} as a contributor to the project "${node.title}" on the DARPA Craft Repository: ${node.absolute_url}

You will ${'not receive ' if all_global_subscriptions_none else 'be automatically subscribed to '} notification emails for this project. To change your email notification preferences, visit your project or your user settings: ${settings.DOMAIN + "settings/notifications/"}

If you are erroneously being associated with "${node.title}," then you may visit the project's "Contributors" page and remove yourself as a contributor.


Sincerely,

DARPA Craft Repository Robot


Want more information? Visit https://osf.io/ to learn about the DARPA Craft Repository, or https://cos.io/ for information about its supporting organization, the Center for Open Science.

Questions? Email contact@osf.io
