const gidBot = GiDBot(API_KEY, PRIVATE_KEY)

gidBot.on('enter_chat', (ctx) => {
    await ctx.sendMessage(`
    Welcome to my small developer conference, the ticket price is 5$.
    For everyone's safety we require a COVID-19 vaccine certificate for attending.`)

    const covidScreening = await ctx.requestScreening(COVID_VACCINE_SCHEMA)
    await ctx.requestPayment({ value: 500, currency: 'USD' })

    const full_name = covidScreening.pii.full_name;
    ctx.issueGroupVerification(
        TICKET_SCHMEA,
        { ticket_id: generateRandomId(), full_name: full_name},
    );
})