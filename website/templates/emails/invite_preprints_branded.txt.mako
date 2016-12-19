<%!
    from website import settings
%>

Hello ${fullname},

You have been added by ${referrer.fullname} as a contributor to the preprint "${node.title}" on ${branded_service_name}, powered by the DARPA Craft Repository. To set a password for your account, visit:

${claim_url}

Once you have set a password, you will be able to make contributions to "${node.title}" and create your own preprints. You will automatically be subscribed to notification emails for this preprint. Each preprint is associated with a project on the DARPA Craft Repository for managing the preprint.  To change your email notification preferences, visit your project or your user settings: ${settings.DOMAIN + "settings/notifications/"}

To preview "${node.title}" click the following link: ${node.absolute_url}

(NOTE: if this project is private, you will not be able to view it until you have confirmed your account)

Sincerely,

Your ${branded_service.name} and Craft teams

