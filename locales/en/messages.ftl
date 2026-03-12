start = 
    ⭐️ <b>Telegram Stars Payment Demo Bot</b>
    
    This bot demonstrates <b>payment</b>, <b>refund</b>, and <b>balance</b> features with Telegram Stars.
    
    <b>How to pay:</b> use <code>/pay &lt;amount&gt;</code> (1 – 100000) to receive an invoice for that many ⭐️.
    
    <b>Refund options:</b>
    • Single payment: <code>/refund &lt;user_id&gt; &lt;transaction_id&gt;</code>
    • All user payments: <code>/refund &lt;user_id&gt;</code>
    
    <b>Other commands:</b>
    • <code>/balance</code> – View current Stars balance
    • <code>/media &lt;amount&gt;</code> – Send paid media with photo (1 – 25000 ⭐️)
    
    Send a payment command now to generate an invoice.

refund-invalid = 
    ❌ <b>Invalid refund command format!</b>
    
    <b>Usage options:</b>
    • Refund specific payment: <code>/refund &lt;user_id&gt; &lt;transaction_id&gt;</code>
    • Refund all user payments: <code>/refund &lt;user_id&gt;</code>
    
    ℹ️ <b>Examples:</b>
    <code>/refund 123456789 ABC123XYZ</code>
    <code>/refund 123456789</code>

refund-failed = 
    ❌ <b>Refund failed!</b>
    
    🆔 <b>Transaction:</b> <code>{ $tx_short }</code>
    👤 <b>User ID:</b> <code>{ $user_id }</code>
    
    💭 <b>Error details:</b>
    <pre>{ $error }</pre>

charge-already-refunded = 
    💰 <b>Already refunded!</b>
    
    🆔 <b>Transaction:</b> <code>{ $tx_short }</code>
    👤 <b>User ID:</b> <code>{ $user_id }</code>
    
    ℹ️ This payment has already been refunded.

charge-not-found = 
    ❓ <b>Transaction not found!</b>
    
    🆔 <b>Transaction:</b> <code>{ $tx_short }</code>
    👤 <b>User ID:</b> <code>{ $user_id }</code>
    
    ⚠️ The specified transaction does not exist.

refund-success = ✅ <b>Payment successfully refunded!</b>

refund-error = 
    ❌ <b>Failed to refund payment</b>
    
    <pre>{ $error }</pre>

refund-transactions-invalid = 
    ❌ <b>Invalid user ID!</b>
    
    ℹ️ Example: <code>/refund 5616264938</code>

refund-transactions-summary = 
    ✅ <b>Batch refund completed</b>

    👤 <b>User ID:</b> <code>{ $user_id }</code>
    📦 <b>Total transactions:</b> { $scanned }
    ✅ <b>Refunded:</b> { $refunded }
    ⏭️ <b>Skipped:</b> { $skipped }
    ❌ <b>Errors:</b> { $failed }

refund-transactions-error = 
    ❌ <b>Failed to load transactions</b>
    
    <pre>{ $error }</pre>

media-invalid = 
    ❌ <b>Invalid media format!</b>
    
    <b>Usage:</b> Send a photo with caption <code>/media &lt;amount&gt;</code>
    
    ℹ️ Amount must be between 1 and 25000 ⭐️
    ℹ️ <b>Example:</b> <code>/media 100</code>

media-caption = Thank you for your purchase! 💫

payment-success = 
    🎉 <b>Payment successful!</b>
    
    💵 <b>Amount:</b> { $amount }⭐️
    🆔 <b>Transaction ID:</b> <code>{ $transaction_id }</code>

amount-invalid = 
    ❌ <b>Invalid payment amount!</b>
    
    Please send a whole number between <b>1</b> and <b>100000</b> using <code>/pay</code>.
    
    ℹ️ <b>Example:</b> <code>/pay 150</code>

balance-info = 
    💰 <b>Bot (@{ $username }) Stars Balance</b>
    
    💵 Current balance: <b>{ $amount }⭐️</b>

payment-link = <b>Payment link:</b> <a href="{ $link }">{ $link }</a>

invoice-error = 
    ❌ <b>Failed to create payment invoice</b>
    
    <pre>{ $error }</pre>

invoice-description = Payment for services via Telegram Stars.

invoice-label = Stars Payment
invoice-title = Telegram Stars Payment

invoice-title = Stars Payment Example

paid-media-caption = 🔒 <b>Paid media</b>
