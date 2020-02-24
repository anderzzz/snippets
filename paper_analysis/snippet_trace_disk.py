#
# Inner loop to draw trace of disk of import/export fraction
#

# Create Bokeh figure
p = figure(plot_width=650, plot_height=500, toolbar_location='above')

# Pick color for country
color = brewer['PRGn'][n_countries][k_country]

# Draw disks
for k_year in range(n_years):

    # Set size disk
    size = 60 * np.sqrt(df['Production'][k_year])

    # Set the alpha, depends if intermediate year
    if k_year in [0, n_years - 1]:
        alpha = 0.6
    else:
        alpha = 0.1

    # Draw circle
    p.circle(df["Export of Stock"][k_year],
             df["Import of Stock"][k_year],
             fill_color=color, size=size, alpha=alpha)

# Draw trace
p.line(x="Export", y="Import", source=ColumnDataSource({'Export' : df["Export of Stock"],
                                                        'Import' : df["Import of Stock"]}))
