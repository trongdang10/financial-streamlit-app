import streamlit as st
from utils import logo

# Define your calculators dictionary with examples and detailed interpretations
calculators = {
    'Market Cap (Market Capitalization)': {
    'formula': r'Market\ Cap = Current\ Share\ Price \times Total\ Number\ of\ Outstanding\ Shares',
    'example': """
    Suppose a company has a Current Share Price of €50 and Total Number of Outstanding Shares of 1,000,000.

    Market Cap = €50 x 1,000,000 = €50,000,000
    """,
    'interpretation': """
    - **Market Cap (Market Capitalization)**: Market capitalization is the total value of a company's outstanding shares of stock, calculated by multiplying the current share price by the total number of outstanding shares.

    - **Components**:
        - **Current Share Price**: The price at which shares of the company are currently trading in the market.
        - **Total Number of Outstanding Shares**: The total number of shares issued by the company and held by investors, including shares held by insiders, institutional investors, and the public.

    - **Significance**:
        - **Valuation Metric**: Market cap is a key measure used by investors to determine the size and value of a company in the market.
        - **Investor Perception**: Market cap reflects investor sentiment and expectations about a company's future prospects and performance.
        - **Comparative Analysis**: Market cap allows for comparison of companies within the same industry or across different sectors based on their relative size and market value.

    - **Interpretation**:
        - A market cap of €50,000,000 means that the total market value of the company's outstanding shares is €50 million.
        - Market cap can fluctuate based on changes in share price and the number of outstanding shares, impacting the company's ranking and investor perceptions.

    - **Limitations**:
        - Market cap does not account for other factors such as debt, cash reserves, or non-equity securities that may affect the company's overall financial position.
        - Differences in share structures (e.g., multiple share classes) or liquidity issues can impact the accuracy of market cap as a valuation metric.

    - **Use in Financial Analysis**:
        - Analysts use market cap to assess the size, risk, and potential return of investments in a company's stock.
        - Comparative analysis with industry peers or benchmarks helps investors evaluate investment opportunities and portfolio allocation strategies.

    - **Calculation Considerations**:
        - Adjustments may be necessary for changes in share price, stock splits, or changes in the number of outstanding shares that impact the accuracy of market cap calculations.
    """
    },
    'Working Capital': {
    'formula': r'Working\ Capital = Current\ Assets - Current\ Liabilities',
    'example': """
    Suppose a company has Current Assets of €500,000 and Current Liabilities of €300,000.

    Working Capital = €500,000 - €300,000 = €200,000
    """,
    'interpretation': """
    - **Working Capital**: Working capital represents the difference between a company's current assets and its current liabilities. It measures the company's short-term liquidity and its ability to cover short-term obligations with its current assets.

    - **Components**:
        - **Current Assets**: Assets that are expected to be converted into cash or consumed within one year, including cash, accounts receivable, inventory, and prepaid expenses.
        - **Current Liabilities**: Liabilities that are due within one year, including accounts payable, short-term loans, accrued expenses, and taxes payable.

    - **Significance**:
        - **Liquidity Measure**: Positive working capital indicates that a company has more current assets than current liabilities, providing a cushion to meet short-term financial obligations.
        - **Operational Efficiency**: Efficient working capital management ensures that the company can maintain smooth operations, manage cash flow effectively, and seize business opportunities.
        - **Financial Health**: Changes in working capital can signal changes in a company's financial health, operational efficiency, and ability to manage growth and downturns.

    - **Interpretation**:
        - A working capital of €200,000 means that the company has €200,000 more in current assets than in current liabilities.
        - Positive working capital is generally preferred as it indicates the company's ability to meet its short-term obligations.

    - **Limitations**:
        - Working capital does not provide information about the composition or quality of current assets and liabilities, which can vary significantly between companies and industries.
        - Different accounting practices or seasonal fluctuations can affect the interpretation of working capital ratios.

    - **Use in Financial Analysis**:
        - Analysts use working capital ratios to assess a company's liquidity position, operational efficiency, and financial health.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate changes in working capital management practices over time.

    - **Calculation Considerations**:
        - Adjustments may be necessary for changes in business operations, fluctuations in asset or liability values, or changes in accounting policies that impact the accuracy of working capital calculations.
    """
    },
    'D/E Ratio (Debt-to-Equity)': {
    'formula': r'D/E\ Ratio = \frac{Total\ Debt}{Total\ Equity}',
    'example': """
    Suppose a company has Total Debt of €2,000,000 and Total Equity of €1,000,000.

    D/E Ratio = 2.0
    """,
    'interpretation': """
    - **D/E Ratio (Debt-to-Equity)**: The debt-to-equity ratio measures the proportion of total debt to total equity, indicating the extent to which a company is financed by debt relative to shareholders' equity.

    - **Components**:
        - **Total Debt**: The sum of all liabilities that require regular payments, including short-term and long-term debt obligations.
        - **Total Equity**: The total value of shareholders' equity, representing the ownership interest in the company after deducting liabilities.

    - **Significance**:
        - **Financial Leverage**: Higher D/E ratios indicate higher financial leverage and greater reliance on debt financing.
        - **Risk Assessment**: Higher ratios suggest higher financial risk due to increased debt obligations and interest payments.
        - **Investor Perception**: Investors use D/E ratios to assess a company's risk profile, financial stability, and ability to manage debt.

    - **Interpretation**:
        - A D/E ratio of 2.0 means that the company has €2 of debt for every €1 of equity.
        - Lower ratios indicate a less leveraged capital structure, while higher ratios indicate higher leverage and potentially higher risk.

    - **Limitations**:
        - D/E ratios vary widely across industries, making direct comparisons challenging without considering industry norms and benchmarks.
        - The ratio does not provide insights into the terms or conditions of debt, such as interest rates, maturity dates, or debt covenants, which are crucial for understanding financial risk.

    - **Use in Financial Analysis**:
        - Analysts use D/E ratios to evaluate a company's capital structure, financial leverage, and risk exposure.
        - Comparative analysis with industry peers or historical trends helps assess changes in leverage and financial health over time.

    - **Calculation Considerations**:
        - Adjustments may be necessary for non-standard debt or equity items to provide a more accurate reflection of the D/E ratio.
    """
    },
    'P/E Ratio (Price-to-Earnings)': {
    'formula': r'P/E\ Ratio = \frac{Market\ Price\ per\ Share}{Earnings\ per\ Share\ (EPS)}',
    'example': """
    Suppose a company has a Market Price per Share of €50 and Earnings per Share (EPS) of €5.

    P/E Ratio  = 10
    """,
    'interpretation': """
    - **P/E Ratio (Price-to-Earnings)**: The price-to-earnings ratio measures the valuation of a company's stock relative to its earnings per share (EPS). It indicates how much investors are willing to pay per euro of earnings.

    - **Components**:
        - **Market Price per Share**: The current market price of a single share of the company's stock.
        - **Earnings per Share (EPS)**: The portion of a company's profit allocated to each outstanding share of common stock, calculated as Net Income divided by the number of outstanding shares.

    - **Significance**:
        - **Valuation Metric**: P/E ratios help investors assess whether a stock is overvalued, undervalued, or fairly priced in relation to its earnings potential.
        - **Growth Expectations**: Higher P/E ratios often indicate that investors expect higher future growth in earnings, while lower ratios may suggest lower growth expectations or higher perceived risks.
        - **Comparative Analysis**: P/E ratios are used for comparative analysis within the same industry or sector to evaluate relative valuation and investment opportunities.

    - **Interpretation**:
        - A P/E ratio of 10 means that investors are willing to pay €10 for every €1 of earnings per share.
        - Higher ratios typically indicate higher investor expectations for future growth or better prospects, while lower ratios may signal undervaluation or lower growth expectations.

    - **Limitations**:
        - P/E ratios may be influenced by factors such as industry norms, market sentiment, economic conditions, and company-specific factors.
        - The ratio does not consider other valuation metrics or qualitative factors that may impact stock prices.

    - **Use in Financial Analysis**:
        - Analysts use P/E ratios to assess stock valuation, compare investment opportunities, and make informed decisions about buying or selling stocks.
        - Comparative analysis with historical P/E ratios or industry benchmarks helps investors gauge changes in valuation and market sentiment.

    - **Calculation Considerations**:
        - Adjustments may be necessary for non-standard earnings or share structures that impact the accuracy and comparability of P/E ratios across companies.
    """
    },
    'ROE (Return on Equity)': {
    'formula': r'ROE = \frac{Net Income}{Average Shareholders\' Equity}',
    'example': """
    Suppose a company has Net Income of €500,000 and Average Shareholders' Equity of €2,000,000.

    ROE  = 0.25 or 25%
    """,
    'interpretation': """
    - **ROE (Return on Equity)**: Return on equity measures a company's profitability relative to its shareholders' equity. It shows how effectively the company generates profit from the equity invested by shareholders.

    - **Components**:
        - **Net Income**: The company's total earnings or profit after all expenses, taxes, and interest have been deducted from revenue.
        - **Average Shareholders' Equity**: The average value of shareholders' equity over a specific period, calculated as (Beginning Shareholders' Equity + Ending Shareholders' Equity) / 2.

    - **Significance**:
        - **Profitability Measure**: ROE indicates the company's ability to generate profit from shareholders' investments in the business.
        - **Management Efficiency**: Higher ROE ratios suggest effective management of assets and liabilities to maximize returns for shareholders.
        - **Investor Perspective**: Investors use ROE to assess the company's financial performance, compare profitability across companies, and evaluate management effectiveness.

    - **Interpretation**:
        - An ROE of 0.25 or 25% means that for every euro of shareholders' equity invested in the company, it generates €0.25 in net income.
        - Higher ROE ratios are generally preferred as they indicate higher profitability and efficient use of equity.

    - **Limitations**:
        - ROE may be influenced by factors such as industry norms, financial leverage, and accounting practices, which can impact comparability across companies.
        - The ratio does not consider risks associated with equity investments or the sustainability of profit margins over time.

    - **Use in Financial Analysis**:
        - Analysts use ROE to evaluate a company's profitability, financial health, and management efficiency over time.
        - Comparative analysis with industry peers or historical trends helps assess changes in profitability and shareholder value creation.

    - **Calculation Considerations**:
        - Adjustments may be necessary for changes in accounting methods, extraordinary items, or non-recurring income or expenses that affect the accuracy of ROE calculations.
    """
    },
    'Dividend Yield': {
    'formula': r'Dividend\ Yield = \frac{Dividend\ per\ Share}{Market\ Price\ per\ Share} \times 100%',
    'example': """
    Suppose a company pays an annual Dividend per Share of €2 and has a Market Price per Share of €50.

    Dividend Yield =  4%
    """,
    'interpretation': """
    - **Dividend Yield**: Dividend yield measures the annual dividend income earned by shareholders relative to the market price per share of the company's stock. It indicates the percentage return on investment from dividends alone.

    - **Components**:
        - **Dividend per Share**: The total dividends paid out to shareholders divided by the total number of outstanding shares.
        - **Market Price per Share**: The current trading price of a single share in the stock market.

    - **Significance**:
        - **Income Generation**: Dividend yield shows how much income investors receive in the form of dividends relative to the price they paid for the stock.
        - **Investor Preference**: Higher dividend yields may attract income-oriented investors seeking regular income streams, while lower yields may indicate growth-oriented investments.
        - **Risk Considerations**: Dividend yield can reflect the company's financial stability, dividend policy, and ability to generate consistent cash flow.

    - **Interpretation**:
        - A dividend yield of 4% means that investors earn 4% of their investment annually in the form of dividends, relative to the current market price per share.
        - Higher dividend yields are generally favorable for income-seeking investors, but excessively high yields may suggest financial distress or unsustainable dividend payouts.

    - **Limitations**:
        - Dividend yield does not account for capital gains or losses from changes in the stock price, which also affect total returns.
        - The yield may fluctuate based on dividend changes, stock price movements, or market conditions.

    - **Use in Financial Analysis**:
        - Analysts use dividend yield to evaluate the attractiveness of stocks for income investors and compare dividend-paying stocks within the same industry or sector.
        - Comparative analysis with historical dividend yields or industry averages helps assess dividend policy consistency and shareholder returns.

    - **Calculation Considerations**:
        - Adjustments may be necessary for non-standard dividend frequencies, special dividends, or changes in the number of outstanding shares that impact the accuracy of dividend yield calculations.
    """
    },
    'Revenue': {
        'formula': r'Revenue = Number\ of\ Units\ Sold \times Average\ Price\ per\ Unit',
        'example': """
        Suppose a company sells 10,000 units of a product at an average price of €100 per unit in a given period.

        Revenue = 10,000 x €100 = €1,000,000
        """,
        'interpretation': """
        - **Revenue**: Revenue, also known as sales or turnover, refers to the total amount of income generated by a company from its operational activities during a specific period, typically a fiscal quarter or year.

        - **Components**:
            - **Number of Units Sold**: The total quantity of products or services sold by the company during the specified period.
            - **Average Price per Unit**: The average selling price of each unit sold.

        - **Significance**:
            - **Financial Performance**: Revenue is a crucial indicator of a company's ability to generate income from its core business operations.
            - **Growth and Stability**: Increasing revenue generally reflects growth, while consistent revenue indicates stability in sales.

        - **Interpretation**:
            - Revenue of €1,000,000 means the company has earned €1 million from its sales activities within the defined period.
            - Analysts and investors use revenue figures to evaluate a company's growth trajectory, market presence, and competitiveness within its industry.

        - **Limitations**:
            - Revenue does not represent profitability; it is possible for a company to have high revenue but low profitability due to high costs.
            - Revenue figures can be influenced by various factors such as seasonality, pricing strategies, and economic conditions.

        - **Use in Financial Analysis**:
            - Investors analyze revenue trends to assess a company's market position and growth potential.
            - Comparative analysis of revenue figures helps in benchmarking against industry peers and assessing market share.

        - **Calculation Considerations**:
            - Accurate revenue calculation requires reliable sales data and understanding of any adjustments like returns, discounts, or allowances that impact net revenue.
        """
    },
    'Cost of Revenue': {
        'formula': r'Cost\ of\ Revenue = Beginning\ Inventory + Purchases\ During\ the\ Period - Ending\ Inventory',
        'example': """
        Suppose a company has:
        - Beginning Inventory: €200,000
        - Purchases During the Period: €500,000
        - Ending Inventory: €250,000

        Cost of Revenue = €200,000 + €500,000 - €250,000 = €450,000
        """,
        'interpretation': """
        - **Cost of Revenue**: Cost of revenue, also known as cost of goods sold (COGS), represents the direct costs incurred by a company in producing and delivering its products or services to customers during a specific period.

        - **Components**:
            - **Beginning Inventory**: The value of inventory at the beginning of the accounting period.
            - **Purchases During the Period**: Additional inventory purchased or produced during the period.
            - **Ending Inventory**: The value of inventory at the end of the accounting period.

        - **Significance**:
            - **Financial Performance**: Cost of revenue directly impacts a company's gross profit and overall profitability.
            - **Inventory Management**: Efficient management of inventory levels and costs is crucial to optimizing cost of revenue.

        - **Limitations**:
            - Cost of revenue calculations can be influenced by inventory valuation methods (e.g., FIFO, LIFO) and adjustments.
            - Changes in inventory levels and valuation can impact the accuracy of cost of revenue figures.

        - **Use in Financial Analysis**:
            - Analysts use cost of revenue to assess a company's cost management strategies and operational efficiency.
            - Comparing cost of revenue across periods or with industry benchmarks helps identify trends and performance improvements.

        - **Calculation Considerations**:
            - Accurate calculation of cost of revenue requires proper tracking and valuation of inventory, and adherence to accounting standards.
        """
    },
    'Gross Profit': {
        'formula': r'Gross\ Profit = Revenue - Cost\ of\ Revenue',
        'example': """
        Suppose a company has revenue of €1,000,000 and cost of revenue (COGS) of €600,000 in a given period.

        Gross Profit = €1,000,000 - €600,000 = €400,000
        """,
        'interpretation': """
        - **Gross Profit**: Gross profit represents the profit a company makes from its core business activities after deducting the direct costs associated with producing and delivering its products or services.

        - **Components**:
            - **Revenue**: Total income generated from sales or services during a specific period.
            - **Cost of Revenue (COGS)**: Direct costs incurred in producing and delivering products or services, including raw materials, labor costs, and manufacturing overhead.

        - **Significance**:
            - **Financial Performance**: Gross profit is a key indicator of a company's profitability before considering operating expenses.
            - **Margin Analysis**: Gross profit margin (Gross Profit divided by Revenue) shows how efficiently a company manages its production costs relative to its revenue.

        - **Limitations**:
            - Gross profit does not account for all operating expenses such as marketing, administrative costs, or interest expenses.
            - Variations in production costs and pricing strategies can impact gross profit margins.

        - **Use in Financial Analysis**:
            - Investors and analysts use gross profit and gross profit margin to assess a company's operational efficiency and compare profitability across different periods or with industry peers.
            - It helps in evaluating cost management strategies and pricing decisions.

        - **Calculation Considerations**:
            - Accurate calculation of gross profit requires reliable revenue and cost data, and understanding of cost allocation methods.
        """
    },
    'Operating Expenses': {
        'formula': r'Operating\ Expenses = Selling\ and\ Marketing\ Expenses + Research\ and\ Development\ Expenses + General\ and\ Administrative\ Expenses',
        'example': """
        Suppose a company has the following operating expenses:
        - Selling and Marketing Expenses: €200,000
        - Research and Development Expenses: €150,000
        - General and Administrative Expenses: €100,000
        
        Total Operating Expenses = €200,000 + €150,000 + €100,000 = €450,000.
        """,
        'interpretation': """
        - **Operating Expenses**: Operating expenses, also known as OPEX, are the costs associated with running a company’s core business operations on a day-to-day basis. These expenses include selling and marketing costs, research and development (R&D) expenditures, and general administrative costs required to sustain business activities.

        - **Selling and Marketing Expenses**: These expenses encompass all costs related to promoting and selling products or services to customers. Examples include advertising, sales commissions, and marketing campaigns.

        - **Research and Development Expenses**: R&D expenses involve costs incurred by a company to innovate, develop new products or improve existing ones. These costs are essential for maintaining competitiveness and driving future growth.

        - **General and Administrative Expenses**: General and administrative expenses cover the costs of managing the overall business operations, including salaries of non-production personnel, office rent, utilities, and other administrative costs.
       """
    },
    'Operating Expenses': {
        'formula': r'Operating\ Expenses = Selling\ and\ Marketing\ Expenses + Research\ and\ Development\ Expenses + General\ and\ Administrative\ Expenses',
        'example': """
        Suppose a company has the following operating expenses:
        - Selling and Marketing Expenses: €200,000
        - Research and Development Expenses: €150,000
        - General and Administrative Expenses: €100,000
        
        Total Operating Expenses = €200,000 + €150,000 + €100,000 = €450,000.
        """,
        'interpretation': """
        - **Operating Expenses**: Operating expenses, also known as OPEX, are the costs associated with running a company’s core business operations on a day-to-day basis. These expenses include selling and marketing costs, research and development (R&D) expenditures, and general administrative costs required to sustain business activities.

        - **Selling and Marketing Expenses**: These expenses encompass all costs related to promoting and selling products or services to customers. Examples include advertising, sales commissions, and marketing campaigns.

        - **Research and Development Expenses**: R&D expenses involve costs incurred by a company to innovate, develop new products or improve existing ones. These costs are essential for maintaining competitiveness and driving future growth.

        - **General and Administrative Expenses**: General and administrative expenses cover the costs of managing the overall business operations, including salaries of non-production personnel, office rent, utilities, and other administrative costs.
       """
    },
    'Other Income/Expenses': {
        'formula': r'Other\ Income/Expenses = Total\ Income\ from\ \text{Non-core}\ Activities\ -\ Total\ Expenses\ from\ {Non-core}\ Activities',
        'example': """
        Suppose a company reports the following financial data:
        - Total Income from Non-core Activities: €100,000
        - Total Expenses from Non-core Activities: €20,000
        
        Other Income/Expenses = €100,000 - €20,000 = €80,000.
        """,
        'interpretation': """
        - **Other Income/Expenses**: Other income/expenses refer to gains or losses incurred by a company from activities that are not directly related to its core business operations. It includes income or expenses from non-core activities such as investments, currency exchange gains or losses, asset sales, or litigation settlements.

        - **Total Income from Non-core Activities**: This represents the total revenue generated from activities that are outside the company's primary business operations. It includes any gains or profits realized from these activities.

        - **Total Expenses from Non-core Activities**: These are the expenses incurred as a result of non-core activities. It includes losses, costs, or charges related to investments, restructuring, asset impairments, or other non-operational activities.
       """
    },
    'Income Before Tax': {
        'formula': r'Income\ Before\ Tax = Revenue\ -\ Cost\ of\ Revenue\ -\ Operating\ Expenses\ +\ Other\ Income/Expenses',
        'example': """
        Suppose a company reports the following financial data:
        - Revenue: €500,000
        - Cost of Revenue: €300,000
        - Operating Expenses: €150,000
        - Other Income/Expenses: €10,000
        
        Income Before Tax = €500,000 - €300,000 - €150,000 + €10,000 = €60,000.
        """,
        'interpretation': """
        - **Income Before Tax**: Income before tax, also known as pre-tax income or profit before tax, represents a company's earnings before deducting income taxes. It is calculated by subtracting operating expenses, cost of revenue, and adding other income/expenses to revenue.

        - **Revenue**: Revenue, also referred to as sales or turnover, is the total amount of money generated from business operations before deducting expenses.

        - **Cost of Revenue**: Cost of revenue includes all costs directly related to producing the goods or services sold by a company, such as materials, labor, and overhead expenses.

        - **Operating Expenses**: Operating expenses are the costs incurred from normal business operations, including salaries, rent, utilities, and other day-to-day expenses.

        - **Other Income/Expenses**: Other income/expenses are gains or losses from activities not directly related to core business operations, such as investment income, currency exchange gains or losses, or asset sales.
        """
    },
    'Tax Income/Expenses': {
        'formula': r'Tax\ Income/Expenses = Income\ Before\ Tax\ -\ Income\ Tax\ Expense',
        'example': """
        Suppose a company reports the following financial data:
        - Income Before Tax: €100,000
        - Income Tax Expense: €20,000
        
        Tax Income/Expenses = €100,000 - €20,000 = €80,000.
        """,
        'interpretation': """
        - **Tax Income/Expenses**: Tax income/expenses, also known as income tax provision or tax expense, represents the amount of taxes a company owes to the government based on its income before tax. It is calculated by subtracting income tax expense from income before tax.

        - **Income Before Tax**: Income before tax is the company's earnings before deducting income taxes. It reflects the profitability of the company's operations before the impact of taxes.

        - **Income Tax Expense**: Income tax expense is the amount of taxes payable based on the taxable income of the company. It is calculated in accordance with tax laws and regulations applicable to the jurisdiction in which the company operates.
        """
    },
    'Net Income': {
        'formula': r'Net\ Income = Revenue\ -\ Expenses',
        'example': """
        Suppose a company reports the following financial data:
        - Revenue: €500,000
        - Expenses: €350,000
        
        Net Income = €500,000 - €350,000 = €150,000.
        """,
        'interpretation': """
        - **Net Income**: Net income, also known as net profit or net earnings, is the amount of profit a company has earned after deducting all expenses from total revenue. It is a key indicator of a company's profitability and financial performance over a specific period.

        - **Revenue**: Revenue represents the total amount of income generated from primary business activities, such as sales of goods or services, before deducting any expenses.

        - **Expenses**: Expenses include all costs incurred by the company in generating revenue and running its operations, such as cost of goods sold, operating expenses, interest expenses, and taxes.
        """
    },
    'Market Performance': {
        'formula': r'Market\ Performance = \frac{Current\ Price - Initial\ Price}{Initial\ Price} \times 100\%',
        'example': """
        Suppose a stock had an initial price of €100 and its current price is €120.
        
        Market Performance = 20\%.
        """,
        'interpretation': """
        - **Market Performance**: Market performance measures the change in the price of a stock, index, or asset over a specified period. It is calculated by determining the percentage increase or decrease from the initial price to the current price.

        - **Current Price**: The current price refers to the most recent trading price of a stock or asset in the market.

        - **Initial Price**: The initial price is the price of the stock or asset at the beginning of the specified period.
        """
    },
    'Profitability Margins': {
        'formula': r'''
        \begin{align*}
        \text{Gross Profit Margin} & = \frac{\text{Gross Profit}}{\text{Revenue}} \times 100\% \\
        \\
        \text{Operating Profit (EBIT) Margin} & = \frac{\text{Operating Income}}{\text{Revenue}} \times 100\% \\
        \\
        \text{Net Profit Margin} & = \frac{\text{Net Income}}{\text{Revenue}} \times 100\%
        \end{align*}
        ''',
        'example': """
        Suppose a company has the following financial figures:
        - Revenue: €1,000,000
        - Gross Profit: €300,000
        - Operating Income: €150,000
        - Net Income: €100,000
        
        Calculating the profitability margins:
        - Gross Profit Margin = 30\%
        - Operating Profit (EBIT) Margin = 15\%
        - Net Profit Margin = 10\%
        """,
        'interpretation': """
        - **Profitability Margins**: Profitability margins are financial ratios that measure a company's profitability relative to its revenue. They provide insights into different stages of profitability:
          - **Gross Profit Margin**: Measures the proportion of revenue remaining after deducting the cost of goods sold (COGS). It reflects the efficiency of production or service delivery.
          - **Operating (EBIT) Profit Margin**: Indicates the proportion of revenue remaining after deducting operating expenses. It shows the company's ability to generate profits from core operations.
          - **Net Profit Margin**: Represents the proportion of revenue remaining after deducting all expenses, including taxes and interest. It indicates the overall profitability of the company.
        """
    },
    'Balance Sheet': {
        'example': """
        The balance sheet provides a snapshot of a company's financial position at a specific point in time. It consists of the following key components:
        
        - **Assets**: These are resources owned by the company, including tangible items like cash, inventory, and property, as well as intangible assets such as patents and goodwill.
        
        - **Liabilities**: These represent the company's obligations or debts, including accounts payable, loans, and bonds.
        
        - **Equity**: Equity represents the difference between assets and liabilities, indicating the net worth of the company attributable to its shareholders.
        
        Example:
        If a company's balance sheet shows:
        - Assets: €1,000,000
        - Liabilities: €500,000
        - Equity: €500,000
        
        This means the company has €1,000,000 in total assets, with €500,000 funded by creditors (liabilities) and €500,000 by shareholders (equity).
        """,
        'interpretation': """
        - **Balance Sheet**: The balance sheet is a financial statement that provides a snapshot of a company's assets, liabilities, and equity at a specific point in time. It illustrates the company's financial position and helps stakeholders understand its liquidity, solvency, and overall financial health.
        
        - **Assets**: Assets are resources owned by the company that provide future economic benefits. They are categorized as current assets (short-term) and non-current assets (long-term).
        
        - **Liabilities**: Liabilities are the company's obligations or debts that must be settled in the future. Like assets, they are classified as current liabilities (due within one year) and non-current liabilities (due after one year).
        
        - **Equity**: Equity represents the shareholders' ownership interest in the company's assets after deducting liabilities. It includes share capital, retained earnings, and other reserves.
        """
    },
    'Assets': {
    'formula': r'Assets = Liabilities + Equity',
    'example': """
    Suppose a company has total liabilities of €50,000 and equity of €150,000.

    Assets = €50,000 + €150,000 = €200,000.
    """,
    'interpretation': """
    - **Assets**: Assets represent everything of value that a company owns or controls, including cash, inventory, equipment, and intellectual property.

    - **Liabilities**: Liabilities are obligations that a company owes to external parties, such as loans, accounts payable, and accrued expenses.

    - **Equity**: Equity represents the residual value of assets after deducting liabilities. It is what remains for the owners or shareholders of the company.

    - **Relative concepts**:
        - **Current Assets**: are assets that are expected to be converted into cash or consumed within a year or the operating cycle of the business, whichever is longer. Examples include cash, accounts receivable, and inventory.
        - **Fixed assets**, also known as long-term assets or property, plant, and equipment (PP&E), are tangible assets that have a useful life of more than one year. Examples include buildings, machinery, and vehicles.
        - **Intangible Assets**: are non-physical assets that have a monetary value but no physical substance. Examples include patents, trademarks, goodwill, and intellectual property.
    """
    },
    'Liabilities': {
    'formula': r'Liabilities = Assets - Equity',
    'example': """
    Suppose a company has total assets of €200,000 and equity of €150,000.

    Liabilities = €200,000 - €150,000 = €50,000.
    """,
    'interpretation': """
    - **Liabilities**: Liabilities are obligations that a company owes to external parties, such as loans, accounts payable, and accrued expenses. They represent claims against the company's assets.

    - **Assets**: Assets represent everything of value that a company owns or controls, including cash, inventory, equipment, and intellectual property.

    - **Equity**: Equity represents the residual value of assets after deducting liabilities. It is what remains for the owners or shareholders of the company.

    - **Relative concepts**:
        - **Current Liabilities**: are obligations due within one year or the operating cycle of the business, whichever is longer. Examples include accounts payable, short-term loans, and accrued expenses.
        - **Long-term Liabilities**: are obligations that are due beyond one year or the operating cycle. Examples include long-term loans, bonds payable, and deferred tax liabilities.
        - **Contingent Liabilities**: are potential liabilities that may arise depending on the outcome of a future event. Examples include guarantees, warranties, and pending lawsuits.
    """
    },
    'Equity': {
    'formula': r'Equity = Assets - Liabilities',
    'example': """
    Suppose a company has total assets of €200,000 and total liabilities of €50,000.

    Equity = €200,000 - €50,000 = €150,000.
    """,
    'interpretation': """
    - **Equity**: Equity represents the residual value of assets after deducting liabilities. It is the ownership interest in the assets of a business.

    - **Assets**: Assets represent everything of value that a company owns or controls, including cash, inventory, equipment, and intellectual property.

    - **Liabilities**: Liabilities are obligations that a company owes to external parties, such as loans, accounts payable, and accrued expenses.

    - **Components of Equity**:
        - **Share Capital**: This includes the funds contributed by shareholders in exchange for shares issued by the company.
        - **Retained Earnings**: These are the accumulated profits of the company that have not been distributed to shareholders as dividends.
        - **Reserves**: These are funds set aside from profits for specific purposes, such as contingency reserves, capital reserves, or statutory reserves.

    - **Role of Equity**: Equity serves as a measure of the company's net worth and the owners' stake in the business. It also reflects the company's ability to withstand financial setbacks and pursue growth opportunities.

    - **Importance in Financial Analysis**: Analysts often look at the composition and trend of equity over time to assess the financial health and stability of a company. Changes in equity can indicate profitability, dividend policy, and management's capital allocation decisions.
    """
    },
    'ROE (Return on Equity)': {
    'formula': r'ROE = \frac{Net\ Income}{Average\ Shareholders\'\ Equity}',
    'example': """
    Suppose a company has a net income of €20,000 and average shareholders' equity of €100,000.

    ROE = 20\%.
    """,
    'interpretation': """
    - **ROE (Return on Equity)**: ROE measures the profitability of a company in relation to the equity invested by shareholders.

    - **Formula**: ROE is calculated as the ratio of net income to average shareholders' equity. It is expressed as a percentage.

    - **Components**:
        - **Net Income**: This is the company's profit after deducting all expenses, taxes, and interest payments.
        - **Average Shareholders' Equity**: This is typically calculated as the average of the shareholders' equity at the beginning and end of a period.

    - **Significance**: ROE indicates how effectively a company generates profit from the equity invested by shareholders. A higher ROE generally indicates better profitability and efficiency in using equity capital.

    - **Comparison**: ROE can be compared across companies within the same industry or over time for the same company to assess performance and management effectiveness.

    - **Limitations**: ROE should be interpreted in conjunction with other financial metrics as it can be influenced by financial leverage and industry norms. A high ROE may also reflect a high-risk strategy.

    - **Use in Analysis**: Investors and analysts use ROE to evaluate the financial health and performance of a company, as it provides insights into management's ability to generate returns on shareholders' investments.
    """
    },
    'ROA': {
    'formula': r'ROA = \frac{Net\ Income}{Average\ Total\ Assets}',
    'example': """
    Suppose a company has a net income of €30,000 and average total assets of €200,000.

    ROA = 15%.
    """,
    'interpretation': """
    - **ROA (Return on Assets)**: ROA measures the profitability of a company relative to its total assets.

    - **Formula**: ROA is calculated as the ratio of net income to average total assets. It is expressed as a percentage.

    - **Components**:
        - **Net Income**: This is the company's profit after deducting all expenses, taxes, and interest payments.
        - **Average Total Assets**: This is typically calculated as the average of the total assets at the beginning and end of a period.

    - **Significance**: ROA indicates how effectively a company generates profit from its assets. It reflects management's efficiency in utilizing assets to generate earnings.

    - **Comparison**: ROA can be compared across companies within the same industry or over time for the same company to assess operational efficiency and profitability.

    - **Use in Analysis**: Investors and analysts use ROA to evaluate the operational performance and profitability of a company. A higher ROA generally indicates better efficiency in asset utilization.

    - **Limitations**: ROA should be interpreted in the context of industry norms and the company's capital structure. Different industries may have different asset turnover rates and capital intensity.

    - **Interpretation**: A declining ROA over time may indicate declining efficiency or profitability, while an increasing ROA may signal improved operational performance.

    - **Adjustments**: ROA can be adjusted for non-operating items or unusual expenses to provide a clearer picture of core operational profitability.
    """
    },
    'Free Cash Flow': {
    'formula': r'Free\ Cash\ Flow = Net\ Cash\ from\ Operating\ Activities - Capital\ Expenditures',
    'example': """
    Suppose a company has net cash from operating activities of €500,000 and capital expenditures of €200,000.

    Free Cash Flow = €500,000 - €200,000 = €300,000.
    """,
    'interpretation': """
    - **Free Cash Flow**: Free cash flow (FCF) represents the cash generated by a business that is available for distribution to debt and equity holders, or for reinvestment in the business.

    - **Net Cash from Operating Activities**: This includes the cash generated or used in the normal course of business operations, excluding cash flows from investing and financing activities.

    - **Capital Expenditures**: Capital expenditures (CapEx) are expenditures incurred to acquire or improve long-term assets such as property, plant, and equipment.

    - **Significance of Free Cash Flow**:
        - **Financial Health**: FCF indicates a company's ability to generate cash from its core operations after accounting for necessary investments in long-term assets.
        - **Investment Potential**: Investors often use FCF to assess a company's ability to pay dividends, reduce debt, buy back stock, or pursue growth opportunities.
        - **Operational Efficiency**: Positive and growing FCF can signal effective management of working capital and capital expenditures.

    - **Calculation Considerations**: Analysts may adjust FCF calculations to account for non-recurring items, changes in working capital, or other factors affecting cash flow stability.

    - **Use in Valuation**: FCF is a key metric in valuation models such as discounted cash flow (DCF) analysis, where it helps determine the intrinsic value of a company's equity.

    - **Limitations**: FCF should be interpreted alongside other financial metrics to provide a comprehensive view of a company's financial performance and prospects.
    """
    },
    'Cash from Operating Activities': {
    'formula': r'Cash\ from\ Operating\ Activities = Net\ Income + \text{Non-cash}\ Expenses - Changes\ in\ Working\ Capital',
    'example': """
    Suppose a company has a net income of €300,000, non-cash expenses (such as depreciation) totaling €50,000, and changes in working capital resulting in an increase of €20,000.

    Cash from Operating Activities = €300,000 + €50,000 - €20,000 = €330,000.
    """,
    'interpretation': """
    - **Cash from Operating Activities**: Cash from operating activities represents the cash generated or used by a company's normal business operations, excluding cash flows from investing and financing activities.

    - **Components**:
        - **Net Income**: Net income is the company's total earnings, calculated by subtracting expenses from revenues.
        - **Non-cash Expenses**: These are expenses that reduce net income but do not involve cash outflow, such as depreciation and amortization.
        - **Changes in Working Capital**: Working capital changes include adjustments in current assets (like accounts receivable and inventory) and current liabilities (like accounts payable and accrued expenses).

    - **Importance**:
        - **Financial Health**: Positive cash from operating activities indicates the ability to generate cash from core operations.
        - **Sustainability**: Sustainable cash flow from operations is crucial for meeting ongoing operational needs, debt repayment, and dividend payments.
        - **Analytical Insights**: Analysts assess trends in cash from operating activities to evaluate operational efficiency and financial performance stability.

    - **Calculation Adjustments**: Companies may adjust this metric for non-recurring items or changes in accounting policies to better reflect ongoing cash generation capability.

    - **Comparison and Analysis**: Comparing cash from operating activities across periods or against industry benchmarks provides insights into a company's operational strengths and weaknesses.

    - **Limitations**: While important, cash from operating activities should be evaluated alongside other financial metrics to provide a comprehensive view of a company's financial health.
    """
    },
    'Cash from Investing Activities': {
    'formula': r'Cash\ from\ Investing\ Activities = Cash\ Inflows\ from\ Investing - Cash\ Outflows\ from\ Investing',
    'example': """
    Suppose a company received €100,000 from selling equipment and spent €50,000 to purchase new investments.

    Cash from Investing Activities = €100,000 - €50,000 = €50,000.
    """,
    'interpretation': """
    - **Cash from Investing Activities**: Cash from investing activities represents the cash flows related to the purchase and sale of long-term assets and investments.

    - **Components**:
        - **Cash Inflows from Investing**: Includes cash received from the sale of property, plant, equipment, and investments.
        - **Cash Outflows from Investing**: Includes cash paid for the purchase of property, plant, equipment, and investments.

    - **Significance**:
        - **Capital Expenditure**: Cash from investing activities reflects the company's investments in long-term assets and its capacity for capital expenditure.
        - **Strategic Investments**: Analysis of cash flows from investing activities provides insights into a company's strategic decisions and growth initiatives.
        - **Investor Perspective**: Investors use this metric to assess management's capital allocation strategies and evaluate potential future growth prospects.

    - **Calculation Adjustments**: Companies may adjust this metric for non-recurring items or changes in investment strategies to provide a clearer picture of cash flow patterns.

    - **Comparison and Analysis**: Trends in cash from investing activities are evaluated over time and compared with industry benchmarks to assess efficiency and effectiveness of investment decisions.

    - **Limitations**: While important for understanding a company's investment activities, cash from investing activities should be considered alongside other financial metrics for a comprehensive assessment of financial health.
    """
    },
    'Cash from Financing Activities': {
    'formula': r'Cash\ from\ Financing\ Activities = Cash\ Inflows\ from\ Financing - Cash\ Outflows\ from\ Financing',
    'example': """
    Suppose a company received €200,000 from issuing new bonds and paid €50,000 in dividends to shareholders.

    Cash from Financing Activities = €200,000 - €50,000 = €150,000.
    """,
    'interpretation': """
    - **Cash from Financing Activities**: Cash from financing activities represents the cash flows related to transactions with the company's owners and creditors.

    - **Components**:
        - **Cash Inflows from Financing**: Includes cash received from issuing stocks or bonds, and proceeds from borrowing (e.g., loans).
        - **Cash Outflows from Financing**: Includes cash paid for dividends, share repurchases, and repayment of borrowings.

    - **Significance**:
        - **Capital Structure**: Cash from financing activities reflects the company's financing decisions and its capital structure management.
        - **Investor Impact**: Investors analyze this metric to understand how a company funds its operations and growth, and how it returns value to shareholders.
        - **Financial Flexibility**: Trends in cash from financing activities indicate a company's ability to raise capital and manage its financial obligations.

    - **Calculation Adjustments**: Companies may adjust this metric for non-recurring items or changes in financing strategies to provide a clearer view of cash flow dynamics.

    - **Comparison and Analysis**: Trends in cash from financing activities are assessed over time and compared with industry norms to evaluate financial policies and shareholder returns.

    - **Limitations**: While important for understanding a company's financing activities, cash from financing activities should be evaluated alongside other financial metrics for a comprehensive assessment of financial health.
    """
    },
    'Current Ratio': {
    'formula': r'Current\ Ratio = \frac{Current\ Assets}{Current\ Liabilities}',
    'example': """
    Suppose a company has current assets of €500,000 and current liabilities of €250,000.

    Current Ratio = 2.
    """,
    'interpretation': """
    - **Current Ratio**: The current ratio measures the ability of a company to meet its short-term obligations with its short-term assets. It is a liquidity ratio.

    - **Components**:
        - **Current Assets**: Assets expected to be converted into cash or consumed within one year, such as cash, accounts receivable, and inventory.
        - **Current Liabilities**: Obligations due within one year, including accounts payable, short-term debt, and accrued expenses.

    - **Significance**:
        - **Liquidity Assessment**: A current ratio above 1 indicates the company has more current assets than current liabilities, suggesting it can cover its short-term obligations.
        - **Financial Health**: Higher current ratios are generally preferred, as they indicate a stronger ability to meet short-term financial commitments.
        - **Industry Comparison**: The ratio should be compared with industry benchmarks to assess liquidity relative to peers.

    - **Interpretation**:
        - A current ratio of 2 means the company has €2 in current assets for every €1 in current liabilities, which is considered healthy in many industries.
        - Ratios significantly above or below 1 may indicate potential issues with liquidity or inefficient use of assets.

    - **Limitations**:
        - The current ratio does not provide insights into the quality of current assets or the timing of cash inflows and outflows.
        - Changes in industry dynamics or seasonal fluctuations can affect the interpretation of the current ratio.

    - **Use in Financial Analysis**:
        - Analysts use the current ratio along with other liquidity ratios to assess a company's short-term financial health and risk.
        - Trends in the current ratio over time can indicate improvements or deteriorations in liquidity management.

    - **Calculation Considerations**:
        - Companies with highly seasonal operations may have varying current ratios throughout the year, requiring careful interpretation.
    """
    },
    'Quick Ratio': {
    'formula': r'Quick\ Ratio = \frac{Current\ Assets - Inventory}{Current\ Liabilities}',
    'example': """
    Suppose a company has current assets of €500,000, including €100,000 in inventory, and current liabilities of €250,000.

    Quick Assets = Current Assets - Inventory = €500,000 - €100,000 = €400,000

    Quick Ratio = 1.6
    """,
    'interpretation': """
    - **Quick Ratio**: The quick ratio, also known as the acid-test ratio, measures the ability of a company to meet its short-term obligations using its most liquid assets.

    - **Components**:
        - **Quick Assets**: Current assets that can be quickly converted into cash without significant loss of value, typically excluding inventory. Examples include cash, marketable securities, and accounts receivable.
        - **Current Liabilities**: Obligations due within one year, such as accounts payable, short-term debt, and accrued expenses.

    - **Significance**:
        - **Liquidity Assessment**: The quick ratio provides a more stringent test of liquidity compared to the current ratio because it excludes inventory, which may not be easily convertible into cash.
        - **Financial Health**: A higher quick ratio (ideally 1 or higher) indicates a stronger ability to meet short-term obligations using readily available liquid assets.
        - **Risk Management**: Investors and creditors use the quick ratio to assess the risk of a company facing liquidity issues in the short term.

    - **Interpretation**:
        - A quick ratio of 1.6 means the company has €1.60 in quick assets for every €1 in current liabilities, which suggests good liquidity coverage.
        - Ratios significantly below 1 may indicate potential difficulties in meeting short-term obligations without relying on selling inventory.

    - **Limitations**:
        - The quick ratio may vary widely across industries, and a low ratio may be acceptable in some sectors with efficient inventory management practices.
        - Changes in business operations or industry dynamics can affect the interpretation of the quick ratio.

    - **Use in Financial Analysis**:
        - Analysts use the quick ratio alongside other liquidity ratios to gain insights into a company's ability to manage short-term financial obligations.
        - Comparisons with industry benchmarks and historical trends help assess improvements or deteriorations in liquidity management.

    - **Calculation Considerations**:
        - Companies with highly seasonal sales or inventory management challenges may see fluctuations in their quick ratio, necessitating careful analysis over time.
    """
    },
    'Cash Ratio': {
    'formula': r'Cash\ Ratio = \frac{Cash\ and\ Cash\ Equivalents}{Current\ Liabilities}',
    'example': """
    Suppose a company has cash and cash equivalents totaling €150,000 and current liabilities of €100,000.

    Cash Ratio = 1.5
    """,
    'interpretation': """
    - **Cash Ratio**: The cash ratio measures the ability of a company to cover its short-term liabilities using only its cash and cash equivalents.

    - **Components**:
        - **Cash and Cash Equivalents**: Includes cash on hand and assets that are easily convertible into cash within a very short time frame, typically within 90 days or less.
        - **Current Liabilities**: Obligations due within one year, such as accounts payable, short-term debt, and accrued expenses.

    - **Significance**:
        - **Strict Liquidity Test**: The cash ratio provides the strictest measure of liquidity because it focuses solely on cash and highly liquid assets.
        - **Risk Assessment**: A higher cash ratio (ideally 1 or higher) indicates a stronger ability to cover short-term obligations with readily available cash.
        - **Financial Health**: Investors and creditors use the cash ratio to assess the immediate liquidity risk of a company.

    - **Interpretation**:
        - A cash ratio of 1.5 means the company has €1.50 in cash and cash equivalents for every €1 in current liabilities, which suggests robust liquidity.
        - Ratios significantly below 1 may indicate potential difficulties in meeting short-term obligations without relying on other liquid assets.

    - **Limitations**:
        - The cash ratio does not consider the availability of other liquid assets like accounts receivable or marketable securities, which could also be used to meet short-term obligations.
        - Changes in cash flow patterns or unexpected cash outflows can impact the interpretation of the cash ratio.

    - **Use in Financial Analysis**:
        - Analysts use the cash ratio alongside other liquidity ratios to evaluate a company's ability to manage short-term financial obligations.
        - Comparative analysis with industry benchmarks and historical trends helps assess liquidity management practices.

    - **Calculation Considerations**:
        - Companies with stable cash flow and conservative financial policies typically maintain higher cash ratios, providing a buffer against unexpected cash needs.
    """
    },
    'Days Sales Outstanding (DSO)': {
    'formula': r'DSO = \frac{Accounts\ Receivable}{Average\ Daily\ Sales}',
    'example': """
    Suppose a company has accounts receivable of €100,000 and average daily sales of €10,000.

    DSO = 10 days
    """,
    'interpretation': """
    - **Days Sales Outstanding (DSO)**: DSO measures the average number of days it takes for a company to collect payment from its customers after a sale is made.

    - **Components**:
        - **Accounts Receivable**: The total amount of money owed to the company by customers for goods or services sold on credit.
        - **Average Daily Sales**: The average amount of sales made by the company per day over a specific period.

    - **Significance**:
        - **Efficiency of Receivables Collection**: A lower DSO indicates that the company collects payments from customers more quickly, which improves cash flow and liquidity.
        - **Working Capital Management**: Effective management of DSO helps in optimizing working capital by reducing the time between making a sale and receiving cash.
        - **Customer Credit Policies**: Changes in DSO can reflect changes in customer credit policies or the effectiveness of credit and collections management.

    - **Interpretation**:
        - A DSO of 10 days means, on average, it takes the company 10 days to collect payments from customers after making a sale.
        - Longer DSO may indicate issues with credit policies, collections processes, or customer financial health.

    - **Limitations**:
        - DSO calculations can be influenced by seasonal sales patterns or one-time events, which may distort the true average collection period.
        - Differences in industry practices can affect the comparability of DSO across companies.

    - **Use in Financial Analysis**:
        - Analysts use DSO to assess the efficiency of receivables management and its impact on cash flow and liquidity.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate improvements or deteriorations in receivables collection.

    - **Calculation Considerations**:
        - Adjustments may be needed for seasonal variations in sales or changes in credit terms to provide a more accurate reflection of receivables management efficiency.
    """
    },
    'Days of Inventory Outstanding (DIO)': {
    'formula': r'DIO = \frac{Average\ Inventory}{Cost\ of\ Goods\ Sold\ (COGS) / 365}',
    'example': """
    Suppose a company has average inventory worth €200,000 and annual Cost of Goods Sold (COGS) of €500,000.

    DIO = 146 days
    """,
    'interpretation': """
    - **Days of Inventory Outstanding (DIO)**: DIO measures the average number of days it takes for a company to sell its inventory.

    - **Components**:
        - **Average Inventory**: The average value of inventory held by the company over a specific period, typically calculated as (Beginning Inventory + Ending Inventory) / 2.
        - **Cost of Goods Sold (COGS)**: The total cost incurred by the company to produce or purchase goods sold during a specific period.

    - **Significance**:
        - **Inventory Management**: Lower DIO indicates efficient inventory management and turnover, reducing holding costs and potential obsolescence.
        - **Working Capital Efficiency**: Effective management of DIO helps optimize working capital by minimizing tied-up capital in inventory.
        - **Operational Efficiency**: Changes in DIO can reflect improvements or challenges in production planning, sales forecasts, or supply chain management.

    - **Interpretation**:
        - A DIO of 146 days means, on average, it takes the company 146 days to sell its inventory.
        - Shorter DIO is generally preferred, as it indicates faster turnover of inventory and better liquidity management.

    - **Limitations**:
        - DIO calculations may be influenced by seasonal demand, changes in production cycles, or shifts in customer preferences, which can affect inventory turnover rates.
        - Industry norms and company-specific factors should be considered when interpreting DIO.

    - **Use in Financial Analysis**:
        - Analysts use DIO to evaluate inventory management efficiency and its impact on cash flow, profitability, and financial health.
        - Comparative analysis with industry benchmarks or historical trends helps assess improvements or deteriorations in inventory turnover.

    - **Calculation Considerations**:
        - Adjustments may be needed for significant changes in inventory valuation methods, production processes, or sales strategies that impact DIO calculations.
    """
    },
    'Operating Cycle': {
    'formula': r'Operating\ Cycle = DIO + DSO',
    'example': """
    Suppose a company has Days of Inventory Outstanding (DIO) of 60 days and Days Sales Outstanding (DSO) of 30 days.

    Operating Cycle = 60 days (DIO) + 30 days (DSO) = 90 days
    """,
    'interpretation': """
    - **Operating Cycle**: The operating cycle measures the average number of days it takes for a company to convert its inventory into cash through sales.

    - **Components**:
        - **Days of Inventory Outstanding (DIO)**: The average number of days it takes for the company to sell its inventory, as calculated previously.
        - **Days Sales Outstanding (DSO)**: The average number of days it takes for the company to collect payment from its customers after a sale.

    - **Significance**:
        - **Efficiency of Operations**: The operating cycle indicates how efficiently a company manages its working capital by measuring the time it takes to convert inventory into cash.
        - **Cash Flow and Liquidity**: Shorter operating cycles generally imply faster cash conversion, which improves liquidity and financial flexibility.
        - **Operational Effectiveness**: Changes in the operating cycle can highlight improvements or challenges in inventory management, sales efficiency, and receivables collection.

    - **Interpretation**:
        - An operating cycle of 90 days means, on average, it takes the company 90 days to complete one cycle from purchasing inventory to receiving cash from sales.
        - Companies aim to shorten their operating cycle to optimize cash flow and working capital management.

    - **Limitations**:
        - The operating cycle may vary widely across industries and company sizes, making direct comparisons challenging without considering industry norms.
        - External factors such as economic conditions or competitive pressures can impact the operating cycle.

    - **Use in Financial Analysis**:
        - Analysts use the operating cycle to assess operational efficiency, working capital requirements, and cash flow dynamics.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate improvements or deteriorations in operational effectiveness.

    - **Calculation Considerations**:
        - Adjustments may be necessary for changes in business operations, production cycles, or sales strategies that affect the components of the operating cycle.
    """
    },
    'Days Payables Outstanding (DPO)': {
    'formula': r'DPO = \frac{Accounts\ Payable}{Cost\ of\ Goods\ Sold\ (COGS) / 365}',
    'example': """
    Suppose a company has accounts payable of €80,000 and annual Cost of Goods Sold (COGS) of €400,000.

    DPO = 73 days
    """,
    'interpretation': """
    - **Days Payables Outstanding (DPO)**: DPO measures the average number of days it takes for a company to pay its suppliers for purchases made on credit.

    - **Components**:
        - **Accounts Payable**: The total amount of money owed by the company to suppliers and vendors for goods or services purchased on credit.
        - **Cost of Goods Sold (COGS)**: The total cost incurred by the company to produce or purchase goods sold during a specific period.

    - **Significance**:
        - **Supplier Relationship Management**: DPO helps evaluate how efficiently a company manages its supplier payments and its relationship with suppliers.
        - **Working Capital Management**: Longer DPO indicates the company is using supplier financing effectively to manage working capital by delaying payments.
        - **Cash Flow Optimization**: Effective management of DPO can improve cash flow by extending the time before cash outflows for payments are required.

    - **Interpretation**:
        - A DPO of 73 days means, on average, it takes the company 73 days to pay its suppliers for purchases made on credit.
        - Longer DPO may indicate favorable credit terms with suppliers or efficient cash flow management practices.

    - **Limitations**:
        - DPO calculations can be influenced by changes in payment terms negotiated with suppliers or shifts in purchasing patterns, which may affect the accuracy of the metric.
        - Industry norms and company-specific factors should be considered when interpreting DPO.

    - **Use in Financial Analysis**:
        - Analysts use DPO to assess supplier payment practices, working capital efficiency, and cash flow management strategies.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate improvements or deteriorations in payment cycle management.

    - **Calculation Considerations**:
        - Adjustments may be necessary for changes in supplier relationships, purchasing strategies, or fluctuations in COGS that impact DPO calculations.
    """
    },
    'Cash Conversion Cycle (CCC)': {
    'formula': r'CCC = DIO + DSO - DPO',
    'example': """
    Suppose a company has Days of Inventory Outstanding (DIO) of 60 days, Days Sales Outstanding (DSO) of 30 days, and Days Payables Outstanding (DPO) of 45 days.

    CCC = 60 days (DIO) + 30 days (DSO) - 45 days (DPO) = 45 days
    """,
    'interpretation': """
    - **Cash Conversion Cycle (CCC)**: CCC measures the average number of days it takes for a company to convert its investments in inventory and other resources into cash flows from sales, and then back into cash from collecting receivables.

    - **Components**:
        - **Days of Inventory Outstanding (DIO)**: The average number of days it takes for the company to sell its inventory.
        - **Days Sales Outstanding (DSO)**: The average number of days it takes for the company to collect payment from its customers after a sale.
        - **Days Payables Outstanding (DPO)**: The average number of days it takes for the company to pay its suppliers for purchases made on credit.

    - **Significance**:
        - **Working Capital Management**: CCC provides insights into how efficiently a company manages its working capital by evaluating the time it takes to generate cash flows from operations.
        - **Cash Flow Optimization**: Shorter CCC implies faster cash conversion cycles, which can enhance liquidity and financial flexibility.
        - **Operational Efficiency**: Changes in CCC can highlight improvements or challenges in inventory management, receivables collection, and payables management.

    - **Interpretation**:
        - A CCC of 45 days means, on average, it takes the company 45 days to convert its investments in inventory and other resources into cash from sales and then back into cash from collecting receivables.
        - Companies strive to minimize CCC to optimize cash flow and improve operational efficiency.

    - **Limitations**:
        - CCC calculations may be influenced by seasonal fluctuations, changes in production cycles, or shifts in customer and supplier relationships, which can impact the accuracy of the metric.
        - Industry norms and company-specific factors should be considered when interpreting CCC.

    - **Use in Financial Analysis**:
        - Analysts use CCC to assess operational efficiency, working capital requirements, and cash flow dynamics.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate improvements or deteriorations in cash conversion cycle management.

    - **Calculation Considerations**:
        - Adjustments may be necessary for changes in business operations, supply chain dynamics, or financial strategies that affect the components of CCC.
    """
    },
    'Debt Ratio (%)': {
    'formula': r'Debt\ Ratio = \frac{Total\ Debt}{Total\ Assets} \times 100',
    'example': """
    Suppose a company has total debt of €1,000,000 and total assets of €2,500,000.

    Debt Ratio = 40%
    """,
    'interpretation': """
    - **Debt Ratio**: The debt ratio measures the proportion of a company's assets financed by debt rather than equity.

    - **Components**:
        - **Total Debt**: The sum of all liabilities that require regular payments, including short-term and long-term debt obligations.
        - **Total Assets**: The total resources owned by the company, including current and non-current assets.

    - **Significance**:
        - **Financial Leverage**: Debt ratio indicates the extent to which a company relies on debt financing to fund its operations and investments.
        - **Risk Assessment**: Higher debt ratios may indicate higher financial risk due to increased leverage and debt servicing obligations.
        - **Capital Structure**: Debt ratio influences a company's ability to raise additional capital and its cost of capital.

    - **Interpretation**:
        - A debt ratio of 40% means 40% of the company's assets are financed by debt, while the remaining 60% is financed by equity.
        - Comparative analysis with industry averages or historical trends helps assess whether the debt ratio is within acceptable limits for the industry.

    - **Limitations**:
        - Debt ratio does not provide information about the nature or terms of debt, such as interest rates, maturity dates, or covenants.
        - Changes in asset values or accounting practices can affect the interpretation of the debt ratio.

    - **Use in Financial Analysis**:
        - Analysts use debt ratio to evaluate a company's capital structure, financial risk, and ability to meet debt obligations.
        - Trend analysis helps assess changes in leverage over time and potential implications for financial health.

    - **Calculation Considerations**:
        - Adjustments may be needed for non-standard debt items or adjustments in asset valuation to provide a more accurate reflection of the debt ratio.
    """
    },
    'Long-term Debt to Capitalization (%)': {
    'formula': r'\text{Long-term}\ Debt\ to\ Capitalization = \frac{\text{Long-term}\ Debt}{\text{Long-term} Debt + Total Equity} \times 100',
    'example': """
    Suppose a company has long-term debt of €500,000 and total equity of €1,000,000.

    Long-term Debt to Capitalization = 33.33%
    """,
    'interpretation': """
    - **Long-term Debt to Capitalization**: This ratio measures the proportion of long-term debt relative to the total capitalization of a company, including long-term debt and total equity.

    - **Components**:
        - **Long-term Debt**: The portion of a company's debt that matures in more than one year, including bonds, mortgages, and other long-term loans.
        - **Total Equity**: The total value of the company's shareholders' equity, which represents the ownership interest in the company.

    - **Significance**:
        - **Financial Structure**: Long-term debt to capitalization ratio reflects the extent to which a company relies on debt financing relative to equity financing.
        - **Risk Assessment**: Higher ratios indicate higher leverage and potentially higher financial risk due to increased debt servicing obligations.
        - **Investor Perspective**: Investors use this ratio to assess the financial risk and stability of a company's capital structure.

    - **Interpretation**:
        - A long-term debt to capitalization ratio of 33.33% means that 33.33% of the company's capitalization (the sum of long-term debt and total equity) is financed by long-term debt.
        - Lower ratios may indicate a more conservative financial structure, while higher ratios may indicate greater leverage.

    - **Limitations**:
        - The ratio does not provide insights into the terms or conditions of the debt, such as interest rates, maturity dates, or covenants.
        - Changes in market conditions or company-specific factors can impact the interpretation of the ratio.

    - **Use in Financial Analysis**:
        - Analysts use long-term debt to capitalization ratio to evaluate a company's capital structure, financial risk, and ability to manage debt obligations.
        - Comparative analysis with industry benchmarks or historical trends helps assess changes in leverage over time and potential implications for financial health.

    - **Calculation Considerations**:
        - Adjustments may be necessary for non-standard debt items or adjustments in equity components to provide a more accurate reflection of the ratio.
    """
    },
    'Total Debt to Capitalization (%)': {
    'formula': r'Total\ Debt\ to\ Capitalization = \frac{Total\ Debt}{Total\ Debt + Total\ Equity} \times 100',
    'example': """
    Suppose a company has total debt of €800,000 and total equity of €1,500,000.

    Total Debt to Capitalization = 34.78%
    """,
    'interpretation': """
    - **Total Debt to Capitalization**: This ratio measures the proportion of total debt relative to the total capitalization of a company, including total debt and total equity.

    - **Components**:
        - **Total Debt**: The sum of all liabilities that require regular payments, including short-term and long-term debt obligations.
        - **Total Equity**: The total value of the company's shareholders' equity, which represents the ownership interest in the company.

    - **Significance**:
        - **Capital Structure**: Total debt to capitalization ratio indicates the overall financial leverage of a company, reflecting the balance between debt and equity financing.
        - **Financial Risk**: Higher ratios suggest higher leverage and potentially higher financial risk due to increased debt servicing obligations.
        - **Investor Perspective**: Investors use this ratio to assess the risk associated with a company's debt levels and its ability to manage debt repayments.

    - **Interpretation**:
        - A total debt to capitalization ratio of 34.78% means that 34.78% of the company's capitalization (the sum of total debt and total equity) is financed by total debt.
        - Lower ratios may indicate a more conservative financial structure, while higher ratios may indicate greater reliance on debt financing.

    - **Limitations**:
        - The ratio does not provide insights into the specific terms or conditions of the debt, such as interest rates, maturity dates, or covenants.
        - Changes in market conditions or company-specific factors can impact the interpretation of the ratio.

    - **Use in Financial Analysis**:
        - Analysts use total debt to capitalization ratio to evaluate a company's overall capital structure, financial risk, and leverage.
        - Comparative analysis with industry benchmarks or historical trends helps assess changes in leverage over time and potential implications for financial health.

    - **Calculation Considerations**:
        - Adjustments may be necessary for non-standard debt items or adjustments in equity components to provide a more accurate reflection of the ratio.
    """
    },
    'Interest Coverage': {
    'formula': r'Interest\ Coverage = \frac{EBIT}{Interest\ Expense}',
    'example': """
    Suppose a company has Earnings Before Interest and Taxes (EBIT) of €500,000 and Interest Expense of €50,000.

    Interest Coverage = 10
    """,
    'interpretation': """
    - **Interest Coverage**: Interest coverage ratio measures a company's ability to meet its interest payments on debt obligations with its earnings before interest and taxes (EBIT).

    - **Components**:
        - **EBIT (Earnings Before Interest and Taxes)**: This represents the company's operating profit before deducting interest expense and taxes.
        - **Interest Expense**: The cost of borrowing money, typically reported on the income statement.

    - **Significance**:
        - **Financial Health**: Higher interest coverage ratios indicate that the company is more capable of servicing its debt obligations from its operating earnings.
        - **Risk Assessment**: Lower ratios suggest that the company may have difficulty meeting interest payments if earnings decline.
        - **Creditworthiness**: Lenders and investors use interest coverage ratios to assess the company's ability to repay debt and manage financial obligations.

    - **Interpretation**:
        - An interest coverage ratio of 10 means that the company's earnings before interest and taxes are sufficient to cover its interest expense 10 times over.
        - Higher ratios are generally favorable, indicating stronger financial health and lower risk of default on debt obligations.

    - **Limitations**:
        - The ratio does not consider other obligations such as principal repayments, taxes, or capital expenditures, which also impact cash flow.
        - Changes in business conditions or interest rates can affect the sustainability of interest coverage ratios.

    - **Use in Financial Analysis**:
        - Analysts use interest coverage ratios to evaluate a company's ability to manage debt and assess its financial risk.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate changes in financial health and risk management practices.

    - **Calculation Considerations**:
        - Adjustments may be necessary for non-operating items affecting EBIT or unusual fluctuations in interest expense to provide a more accurate reflection of the ratio.
    """
    },
    'Cash Flow to Debt Ratio': {
    'formula': r'Cash\ Flow\ to\ Debt\ Ratio = \frac{Operating\ Cash\ Flow}{Total\ Debt}',
    'example': """
    Suppose a company has Operating Cash Flow of €300,000 and Total Debt of €1,000,000.

    Cash Flow to Debt Ratio = 0.3
    """,
    'interpretation': """
    - **Cash Flow to Debt Ratio**: This ratio measures a company's ability to repay its debt using its operating cash flow.

    - **Components**:
        - **Operating Cash Flow**: The cash generated from the company's core business operations, typically reported on the cash flow statement.
        - **Total Debt**: The sum of all liabilities that require regular payments, including short-term and long-term debt obligations.

    - **Significance**:
        - **Debt Repayment Ability**: Higher cash flow to debt ratios indicate a stronger ability to generate sufficient cash flow to meet debt obligations.
        - **Financial Stability**: A healthy ratio suggests that the company has adequate liquidity and cash flow management to support its debt commitments.
        - **Risk Assessment**: Lower ratios may indicate potential challenges in meeting debt obligations with existing cash flow.

    - **Interpretation**:
        - A cash flow to debt ratio of 0.3 means that for every €1 of total debt, the company generates €0.30 of operating cash flow.
        - Higher ratios are generally favorable, indicating stronger financial health and lower risk in servicing debt.

    - **Limitations**:
        - The ratio does not consider other cash flow needs such as capital expenditures, dividends, or other debt repayments beyond operating cash flow.
        - Changes in business conditions, such as economic downturns or industry-specific challenges, can impact cash flow generation and debt repayment capabilities.

    - **Use in Financial Analysis**:
        - Analysts use cash flow to debt ratios to assess a company's ability to manage debt and evaluate its financial stability.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate changes in financial health and cash flow management practices.

    - **Calculation Considerations**:
        - Adjustments may be necessary for non-operating cash flows or unusual fluctuations in debt levels to provide a more accurate reflection of the ratio.
    """
    },
    'Company Equity Multiplier': {
    'formula': r'Company\ Equity\ Multiplier = \frac{Total\ Assets}{Total\ Equity}',
    'example': """
    Suppose a company has Total Assets of €5,000,000 and Total Equity of €2,000,000.

    Company Equity Multiplier = 2.5
    """,
    'interpretation': """
    - **Company Equity Multiplier**: The company equity multiplier, also known as the equity multiplier or leverage ratio, measures the extent to which a company relies on debt financing relative to its equity.

    - **Components**:
        - **Total Assets**: The total value of all assets owned by the company, including current and non-current assets.
        - **Total Equity**: The total value of the company's shareholders' equity, representing ownership interest in the company after deducting liabilities.

    - **Significance**:
        - **Financial Leverage**: Higher equity multipliers indicate that the company relies more heavily on debt financing to fund its assets.
        - **Risk Assessment**: Higher ratios suggest higher financial risk due to increased debt obligations and leverage.
        - **Return on Equity (ROE)**: Changes in the equity multiplier affect the return on equity, as higher leverage can amplify both gains and losses.

    - **Interpretation**:
        - A company equity multiplier of 2.5 means that for every €1 of equity, the company has €2.5 of total assets, of which €1.5 is financed by debt.
        - Lower ratios indicate a less leveraged capital structure, while higher ratios indicate greater reliance on debt financing.

    - **Limitations**:
        - The ratio does not provide insights into the terms or conditions of debt, such as interest rates, maturity dates, or covenants, which are crucial for understanding financial risk.
        - Changes in asset values or accounting practices can affect the interpretation of the equity multiplier.

    - **Use in Financial Analysis**:
        - Analysts use the equity multiplier to assess a company's capital structure, financial leverage, and risk exposure.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate changes in leverage over time and potential implications for financial health.

    - **Calculation Considerations**:
        - Adjustments may be necessary for non-standard asset or equity items to provide a more accurate reflection of the equity multiplier.
    """
    },
    'Receivables Turnover': {
    'formula': r'Receivables\ Turnover = \frac{Net\ Credit\ Sales}{Average\ Accounts\ Receivable}',
    'example': """
    Suppose a company has Net Credit Sales of €1,000,000 and Average Accounts Receivable of €200,000.

    Receivables Turnover = 5 times
    """,
    'interpretation': """
    - **Receivables Turnover**: The receivables turnover ratio measures how efficiently a company manages its accounts receivable by indicating how many times during a period the receivables are collected and replaced.

    - **Components**:
        - **Net Credit Sales**: Total sales made on credit, excluding cash sales, returns, and allowances.
        - **Average Accounts Receivable**: Average amount of accounts receivable over a specific period, calculated as (Beginning Accounts Receivable + Ending Accounts Receivable) / 2.

    - **Significance**:
        - **Efficiency Indicator**: Higher receivables turnover ratios indicate that the company collects payments from customers more quickly, which improves liquidity and reduces the risk of bad debts.
        - **Cash Flow Management**: Efficient receivables turnover enhances cash flow management by accelerating the conversion of accounts receivable into cash.
        - **Credit Policies**: Changes in receivables turnover can reflect changes in credit policies, customer payment behavior, or economic conditions affecting sales.

    - **Interpretation**:
        - A receivables turnover of 5 times means that, on average, the company collects its outstanding receivables 5 times during the period.
        - Higher ratios are generally favorable, indicating efficient credit and collection practices.

    - **Limitations**:
        - The ratio does not account for the credit quality of receivables or the timing of collections within the period, which can affect the interpretation.
        - Industry norms and company-specific factors should be considered when interpreting receivables turnover ratios.

    - **Use in Financial Analysis**:
        - Analysts use receivables turnover ratios to assess the effectiveness of credit policies, cash flow management, and operational efficiency.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate changes in receivables management practices over time.

    - **Calculation Considerations**:
        - Adjustments may be necessary for changes in business operations, seasonal variations in sales, or fluctuations in accounts receivable that impact the accuracy of the ratio.
    """
    },
    'Payables Turnover': {
    'formula': r'Payables\ Turnover = \frac{Total\ Purchases}{Average\ Accounts\ Payable}',
    'example': """
    Suppose a company has Total Purchases of €2,000,000 and Average Accounts Payable of €400,000.

    Payables Turnover = 5 times
    """,
    'interpretation': """
    - **Payables Turnover**: The payables turnover ratio measures how efficiently a company pays its suppliers for goods and services on credit during a specific period.

    - **Components**:
        - **Total Purchases**: The total amount of purchases made by the company, typically excluding returns, allowances, and discounts.
        - **Average Accounts Payable**: Average amount of accounts payable over a specific period, calculated as (Beginning Accounts Payable + Ending Accounts Payable) / 2.

    - **Significance**:
        - **Supplier Payment Efficiency**: Higher payables turnover ratios indicate that the company pays its suppliers more quickly, which can improve supplier relationships and potentially lead to discounts for early payment.
        - **Cash Flow Management**: Efficient payables turnover helps manage working capital by optimizing the timing of payments, balancing liquidity needs, and reducing financing costs.
        - **Operational Performance**: Changes in payables turnover can reflect changes in purchasing patterns, payment terms negotiated with suppliers, or operational efficiency improvements.

    - **Interpretation**:
        - A payables turnover of 5 times means that, on average, the company pays its suppliers 5 times during the period.
        - Higher ratios are generally favorable, indicating efficient cash management and supplier relationships.

    - **Limitations**:
        - The ratio does not consider the terms or conditions of payables, such as early payment discounts or negotiated credit terms, which can affect the interpretation.
        - Industry norms and company-specific factors should be considered when interpreting payables turnover ratios.

    - **Use in Financial Analysis**:
        - Analysts use payables turnover ratios to assess the effectiveness of supplier management, cash flow management, and operational efficiency.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate changes in payables management practices over time.

    - **Calculation Considerations**:
        - Adjustments may be necessary for changes in business operations, seasonal variations in purchasing, or fluctuations in accounts payable that impact the accuracy of the ratio.
    """
    },
    'Inventory Turnover': {
    'formula': r'Inventory\ Turnover = \frac{Cost\ of\ Goods\ Sold}{Average\ Inventory}',
    'example': """
    Suppose a company has Cost of Goods Sold (COGS) of €1,500,000 and Average Inventory of €300,000.

    Inventory Turnover = 5 times
    """,
    'interpretation': """
    - **Inventory Turnover**: The inventory turnover ratio measures how efficiently a company manages its inventory by indicating how many times during a period the inventory is sold and replaced.

    - **Components**:
        - **Cost of Goods Sold (COGS)**: The direct costs attributable to the production of goods sold by the company, including materials, labor, and overhead expenses.
        - **Average Inventory**: Average amount of inventory held by the company over a specific period, calculated as (Beginning Inventory + Ending Inventory) / 2.

    - **Significance**:
        - **Operational Efficiency**: Higher inventory turnover ratios indicate that the company sells and replaces inventory more quickly, which can improve cash flow and reduce storage costs.
        - **Inventory Management**: Efficient inventory turnover helps minimize obsolete inventory and ensures adequate stock levels to meet customer demand.
        - **Financial Performance**: Changes in inventory turnover can reflect changes in sales volume, production efficiency, or shifts in customer demand patterns.

    - **Interpretation**:
        - An inventory turnover of 5 times means that, on average, the company sells and replaces its inventory 5 times during the period.
        - Higher ratios generally indicate efficient inventory management and turnover.

    - **Limitations**:
        - The ratio does not consider the cost structure of inventory items or variations in pricing, which can affect the interpretation.
        - Industry norms and company-specific factors should be considered when interpreting inventory turnover ratios.

    - **Use in Financial Analysis**:
        - Analysts use inventory turnover ratios to assess inventory management practices, operational efficiency, and financial performance.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate changes in inventory management over time.

    - **Calculation Considerations**:
        - Adjustments may be necessary for changes in business operations, seasonal variations in sales, or fluctuations in inventory levels that impact the accuracy of the ratio.
    """
    },
    'Fixed Asset Turnover': {
    'formula': r'Fixed\ Asset\ Turnover = \frac{Net\ Sales}{Average\ Fixed\ Assets}',
    'example': """
    Suppose a company has Net Sales of €2,000,000 and Average Fixed Assets of €500,000.

    Fixed Asset Turnover = 4 times
    """,
    'interpretation': """
    - **Fixed Asset Turnover**: The fixed asset turnover ratio measures how efficiently a company generates net sales from its fixed assets.

    - **Components**:
        - **Net Sales**: Total sales revenue generated by the company, excluding returns, discounts, and allowances.
        - **Average Fixed Assets**: Average value of fixed assets (such as property, plant, and equipment) owned by the company over a specific period, calculated as (Beginning Fixed Assets + Ending Fixed Assets) / 2.

    - **Significance**:
        - **Asset Utilization**: Higher fixed asset turnover ratios indicate that the company efficiently uses its fixed assets to generate sales revenue.
        - **Operational Efficiency**: Efficient fixed asset turnover reflects effective production and operational processes, maximizing the return on investment in fixed assets.
        - **Financial Performance**: Changes in fixed asset turnover can indicate shifts in production efficiency, capacity utilization, or changes in sales volume.

    - **Interpretation**:
        - A fixed asset turnover of 4 times means that, on average, the company generates €4 in net sales for every €1 invested in fixed assets.
        - Higher ratios generally indicate better utilization of fixed assets and operational efficiency.

    - **Limitations**:
        - The ratio does not consider depreciation or the age and condition of fixed assets, which can affect their productive capacity and the interpretation of the ratio.
        - Industry norms and company-specific factors should be considered when interpreting fixed asset turnover ratios.

    - **Use in Financial Analysis**:
        - Analysts use fixed asset turnover ratios to assess asset utilization, operational efficiency, and the effectiveness of capital investments.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate changes in asset management and operational performance over time.

    - **Calculation Considerations**:
        - Adjustments may be necessary for changes in business operations, capital expenditures, or fluctuations in fixed asset values that impact the accuracy of the ratio.
    """
    },
    'Asset Turnover': {
    'formula': r'Asset\ Turnover = \frac{Net\ Sales}{Average\ Total\ Assets}',
    'example': """
    Suppose a company has Net Sales of €3,000,000 and Average Total Assets of €1,000,000.

    Asset Turnover = 3 times
    """,
    'interpretation': """
    - **Asset Turnover**: The asset turnover ratio measures how efficiently a company utilizes its total assets to generate sales revenue.

    - **Components**:
        - **Net Sales**: Total sales revenue generated by the company, excluding returns, discounts, and allowances.
        - **Average Total Assets**: Average value of total assets owned by the company over a specific period, calculated as (Beginning Total Assets + Ending Total Assets) / 2.

    - **Significance**:
        - **Efficiency Indicator**: Higher asset turnover ratios indicate that the company effectively utilizes its assets to generate sales revenue.
        - **Operational Efficiency**: Efficient asset turnover reflects effective use of resources and operational processes to maximize revenue generation.
        - **Financial Performance**: Changes in asset turnover can indicate shifts in production efficiency, capacity utilization, or changes in sales volume relative to asset investments.

    - **Interpretation**:
        - An asset turnover of 3 times means that, on average, the company generates €3 in net sales for every €1 invested in total assets.
        - Higher ratios generally indicate better asset utilization and operational efficiency.

    - **Limitations**:
        - The ratio does not consider variations in asset quality, depreciation, or the impact of non-operating assets, which can affect the interpretation.
        - Industry norms and company-specific factors should be considered when interpreting asset turnover ratios.

    - **Use in Financial Analysis**:
        - Analysts use asset turnover ratios to assess operational efficiency, asset utilization, and the effectiveness of capital investments.
        - Comparative analysis with industry benchmarks or historical trends helps evaluate changes in asset management and operational performance over time.

    - **Calculation Considerations**:
        - Adjustments may be necessary for changes in business operations, asset valuations, or fluctuations in total asset values that impact the accuracy of the ratio.
    """
    }

}

# Sidebar for navigation
st.sidebar.title("Financial Calculators")
calculator_name = st.sidebar.selectbox("Choose a calculator", list(calculators.keys()))

# Main content
if calculator_name:
    st.title(calculator_name)
    st.subheader("Formula")
    st.latex(calculators[calculator_name]['formula'])
    st.subheader("Example")
    st.write(calculators[calculator_name]['example'])
    st.subheader("Interpretation")
    st.write(calculators[calculator_name]['interpretation'])
    
# logo()

# Run the app
if __name__ == '__main__':
    st.title('')
