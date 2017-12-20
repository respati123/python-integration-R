#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
shinyUI(pageWithSidebar(
  headerPanel("Cars 93"),
  sidebarPanel(),
  mainPanel()
))

# Define server logic required to draw a histogram
shinyServer(function(input, output) {
   
  output$distPlot <- renderPlot({plot(concrete_model2)
    
    # generate bins based on input$bins from ui.R
    
  })
  
})
